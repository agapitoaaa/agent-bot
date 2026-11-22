#!/usr/bin/env python3
"""Ledger's learning memory. Stdlib only. Append-only journals, evidence-gated lessons, honest scorecards.

Files (under trading/, override with TRADING_DIR):
  journal/decisions.jsonl   every decision, logged BEFORE the outcome exists
  journal/outcomes.jsonl    outcome per decision (net of costs, vs benchmark)
  memory/lessons.jsonl      lesson events (create / promote), replayed to get current state
  memory/rules.md           generated summary Ledger reads at the start of every task
  memory/policy.json        owner-controlled thresholds

Why gated: learning from a few trades is mostly learning noise. A lesson may change behaviour only after it
is supported by enough independent decisions (policy.json), and 'rule' status also needs QA review.
"""
import argparse, json, os, sys, datetime, math, collections

ROOT = os.environ.get("TRADING_DIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "trading")
P = lambda *a: os.path.join(ROOT, *a)

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

def read(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return out

def append(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(obj) + "\n")

def policy():
    with open(P("memory", "policy.json")) as f:
        return json.load(f)

def new_id(prefix, path):
    n = len(read(path)) + 1
    return f"{prefix}-{datetime.datetime.now(datetime.timezone.utc):%Y%m%d}-{n:04d}"

# ---------- journal ----------
def add_decision(a):
    if not a.rationale.strip() or not a.counter.strip():
        sys.exit("A decision needs a rationale AND the strongest argument against it.")
    if a.action != "no_trade" and not a.invalidation.strip():
        sys.exit("A trade needs a pre-declared invalidation/exit rule.")
    if a.confidence is not None and not 0 <= a.confidence <= 1:
        sys.exit("confidence must be between 0 and 1")
    path = P("journal", "decisions.jsonl")
    d = {"id": new_id("d", path), "ts": now(), "strategy": a.strategy, "instrument": a.instrument,
         "action": a.action, "size_pct": a.size_pct, "rationale": a.rationale, "evidence": a.evidence or [],
         "invalidation": a.invalidation, "counter": a.counter, "confidence": a.confidence}
    append(path, d)
    print(d["id"])

def add_outcome(a):
    decisions = {d["id"]: d for d in read(P("journal", "decisions.jsonl"))}
    if a.decision not in decisions:
        sys.exit("unknown decision id")
    if any(o["decision_id"] == a.decision for o in read(P("journal", "outcomes.jsonl"))):
        sys.exit("outcome already recorded for this decision (journals are append-only)")
    o = {"decision_id": a.decision, "ts": now(), "pnl_net_pct": a.pnl_net_pct,
         "benchmark_pct": a.benchmark_pct, "hit": a.pnl_net_pct > 0, "notes": a.notes or ""}
    append(P("journal", "outcomes.jsonl"), o)
    print("recorded", a.decision, "net", a.pnl_net_pct)

# ---------- lessons (event sourced) ----------
def lessons_state():
    state = collections.OrderedDict()
    for e in read(P("memory", "lessons.jsonl")):
        if e["type"] == "create":
            state[e["id"]] = {"id": e["id"], "text": e["text"], "status": "observation", "source": e.get("source", ""),
                              "support": list(e.get("support", [])), "contra": list(e.get("contra", [])), "history": [e["ts"]]}
        elif e["type"] == "promote" and e["id"] in state:
            s = state[e["id"]]
            s["status"] = e["to"]
            s["support"] = sorted(set(s["support"]) | set(e.get("support", [])))
            s["contra"] = sorted(set(s["contra"]) | set(e.get("contra", [])))
            s["history"].append(e["ts"])
    return state

def add_lesson(a):
    path = P("memory", "lessons.jsonl")
    lid = new_id("l", path)
    append(path, {"type": "create", "id": lid, "ts": now(), "text": a.text, "source": a.source,
                  "support": a.support or [], "contra": a.contra or []})
    print(lid, "(observation: does not change behaviour)")

def promote(a):
    st = lessons_state()
    if a.id not in st:
        sys.exit("unknown lesson id")
    pol = policy()
    s = st[a.id]
    support = set(s["support"]) | set(a.support or [])
    contra = set(s["contra"]) | set(a.contra or [])
    known = {d["id"] for d in read(P("journal", "decisions.jsonl"))}
    bad = [x for x in support | contra if x not in known]
    if bad:
        sys.exit(f"evidence must reference journaled decisions; unknown: {bad}")
    if a.to == "candidate" and len(support) < pol["candidate_min_support"]:
        sys.exit(f"candidate needs >= {pol['candidate_min_support']} supporting decisions (have {len(support)})")
    if a.to == "rule":
        if len(support) < pol["rule_min_support"]:
            sys.exit(f"rule needs >= {pol['rule_min_support']} supporting decisions (have {len(support)})")
        if len(contra) > pol["rule_max_contra_ratio"] * len(support):
            sys.exit("too many contradicting decisions for a rule")
        if not a.qa_reviewed:
            sys.exit("rule status requires QA review (--qa-reviewed after qa-engineer has signed off)")
    append(P("memory", "lessons.jsonl"), {"type": "promote", "id": a.id, "ts": now(), "to": a.to,
                                          "reason": a.reason, "support": sorted(support), "contra": sorted(contra)})
    print(a.id, "->", a.to)

# ---------- scorecards ----------
def scorecard():
    decisions = {d["id"]: d for d in read(P("journal", "decisions.jsonl"))}
    outcomes = read(P("journal", "outcomes.jsonl"))
    by = collections.defaultdict(list)
    for o in outcomes:
        d = decisions.get(o["decision_id"])
        if d:
            by[d["strategy"]].append((d, o))
    min_n = policy()["min_sample_for_scorecard_claims"]
    rows = []
    for strat, items in sorted(by.items()):
        n = len(items)
        pnl = [o["pnl_net_pct"] for _, o in items]
        ex = [o["pnl_net_pct"] - (o["benchmark_pct"] or 0) for _, o in items]
        rows.append({"strategy": strat, "n_closed": n, "hit_rate": sum(1 for _, o in items if o["hit"]) / n,
                     "mean_net_pct": sum(pnl) / n, "mean_excess_vs_benchmark_pct": sum(ex) / n,
                     "worst_pct": min(pnl), "sample_ok": n >= min_n})
    return rows

def calibration():
    decisions = {d["id"]: d for d in read(P("journal", "decisions.jsonl"))}
    pts = []
    for o in read(P("journal", "outcomes.jsonl")):
        d = decisions.get(o["decision_id"])
        if d and d.get("confidence") is not None:
            pts.append((d["confidence"], 1.0 if o["hit"] else 0.0))
    if not pts:
        return None
    brier = sum((p - y) ** 2 for p, y in pts) / len(pts)
    bins = policy()["calibration_bins"]
    out, lo = [], 0.0
    for hi in bins:
        grp = [(p, y) for p, y in pts if lo < p <= hi or (lo == 0 and p == 0)]
        if grp:
            out.append({"range": f"{lo:.1f}-{hi:.1f}", "n": len(grp), "avg_confidence": sum(p for p, _ in grp) / len(grp),
                        "hit_rate": sum(y for _, y in grp) / len(grp)})
        lo = hi
    return {"n": len(pts), "brier": brier, "bins": out}

def render(write=True):
    st = lessons_state()
    pol = policy()
    by = collections.defaultdict(list)
    for s in st.values():
        by[s["status"]].append(s)
    L = ["# Ledger: active memory (generated by scripts/trade_memory.py; do not edit by hand)", "",
         f"Generated {now()}. Read this at the start of every task.", "",
         "Lessons are gated: only RULES may be applied by default; CANDIDATES may only add caution; OBSERVATIONS never change behaviour.", ""]
    L.append("## Rules (verified)")
    L += [f"- {s['text']}  [{s['id']}, support {len(s['support'])}, contra {len(s['contra'])}]" for s in by["rule"]] or ["- none yet"]
    L.append("\n## Candidates (caution only)")
    L += [f"- {s['text']}  [{s['id']}, support {len(s['support'])}/{pol['rule_min_support']} needed for rule]" for s in by["candidate"]] or ["- none yet"]
    L.append("\n## Recent observations (do not act on these)")
    L += [f"- {s['text']}  [{s['id']}]" for s in by["observation"][-10:]] or ["- none yet"]
    L.append(f"\n## Retired: {len(by['retired'])}")
    L.append("\n## Scorecard (net of costs)")
    sc = scorecard()
    if not sc:
        L.append("- no closed decisions yet")
    for r in sc:
        flag = "" if r["sample_ok"] else f"  WARNING: n < {pol['min_sample_for_scorecard_claims']}, do not draw conclusions"
        L.append(f"- {r['strategy']}: n={r['n_closed']}, hit {r['hit_rate']:.0%}, mean net {r['mean_net_pct']:.2f}%, "
                 f"excess vs benchmark {r['mean_excess_vs_benchmark_pct']:.2f}%, worst {r['worst_pct']:.2f}%{flag}")
    L.append("\n## Calibration (does stated confidence match outcomes?)")
    cal = calibration()
    if not cal:
        L.append("- no data yet")
    else:
        L.append(f"- n={cal['n']}, Brier score {cal['brier']:.3f} (0 is perfect; 0.25 is a coin flip at 50%)")
        L += [f"  - confidence {b['range']}: n={b['n']}, said {b['avg_confidence']:.0%}, actual {b['hit_rate']:.0%}" for b in cal["bins"]]
    L.append("\n## Standing biases to watch (from the plan)\n- Overtrading and cost blindness\n- Falling for a good-looking backtest\n- Confidence that exceeds the evidence")
    text = "\n".join(L) + "\n"
    if write:
        os.makedirs(P("memory"), exist_ok=True)
        with open(P("memory", "rules.md"), "w") as f:
            f.write(text)
    return text

def main(argv=None):
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest="cmd", required=True)
    d = sp.add_parser("add-decision"); d.set_defaults(fn=add_decision)
    d.add_argument("--strategy", required=True); d.add_argument("--instrument", required=True)
    d.add_argument("--action", required=True, choices=["buy", "sell", "hold", "no_trade"])
    d.add_argument("--size-pct", type=float, default=0.0); d.add_argument("--rationale", required=True)
    d.add_argument("--evidence", nargs="*"); d.add_argument("--invalidation", default="")
    d.add_argument("--counter", required=True); d.add_argument("--confidence", type=float)
    o = sp.add_parser("add-outcome"); o.set_defaults(fn=add_outcome)
    o.add_argument("--decision", required=True); o.add_argument("--pnl-net-pct", type=float, required=True)
    o.add_argument("--benchmark-pct", type=float, default=0.0); o.add_argument("--notes")
    l = sp.add_parser("add-lesson"); l.set_defaults(fn=add_lesson)
    l.add_argument("--text", required=True); l.add_argument("--source", default="review")
    l.add_argument("--support", nargs="*"); l.add_argument("--contra", nargs="*")
    r = sp.add_parser("promote"); r.set_defaults(fn=promote)
    r.add_argument("--id", required=True); r.add_argument("--to", required=True, choices=["candidate", "rule", "retired"])
    r.add_argument("--reason", default=""); r.add_argument("--support", nargs="*"); r.add_argument("--contra", nargs="*")
    r.add_argument("--qa-reviewed", action="store_true")
    s = sp.add_parser("scorecard"); s.set_defaults(fn=lambda a: print(json.dumps({"scorecard": scorecard(), "calibration": calibration()}, indent=2)))
    g = sp.add_parser("render"); g.set_defaults(fn=lambda a: print(render()))
    a = p.parse_args(argv)
    a.fn(a)

if __name__ == "__main__":
    main()
