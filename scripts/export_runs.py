#!/usr/bin/env python3
"""Export real run logs (runs/*.jsonl) as one JSON doc per run, for mirroring into the office page's database.

usage: export_runs.py --out DIR [--all] [--commit]
  Writes DIR/<run_id>.json = {"run_id","events":[...],"lines":N,"updatedAt"} for every run whose line count
  differs from state/mirrored.json (or all with --all). Prints the run ids to upload to collection `runlogs`
  (ArtifactData set, doc_id = run id, file_path = DIR/<run_id>.json). With --commit, state/mirrored.json is
  updated so the next export only includes new events: run it AFTER you uploaded successfully.
"""
import argparse, json, os, sys, datetime
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RUNS = os.path.join(ROOT, "runs")
STATE = os.path.join(ROOT, "state", "mirrored.json")

def read_events(path):
    ev = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    o = json.loads(line)
                    if isinstance(o, dict) and o.get("type"):
                        ev.append(o)
                except json.JSONDecodeError:
                    pass
    return ev

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--out", required=True)
    p.add_argument("--all", action="store_true")
    p.add_argument("--commit", action="store_true")
    a = p.parse_args(argv)
    state = {}
    if os.path.exists(STATE):
        with open(STATE) as f:
            state = json.load(f)
    os.makedirs(a.out, exist_ok=True)
    changed, newstate = [], dict(state)
    for name in sorted(os.listdir(RUNS)):
        if not name.endswith(".jsonl"):
            continue
        rid = name[:-6]
        ev = read_events(os.path.join(RUNS, name))
        if not ev:
            continue
        if a.all or state.get(rid) != len(ev):
            doc = {"run_id": rid, "events": ev, "lines": len(ev),
                   "updatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")}
            with open(os.path.join(a.out, rid + ".json"), "w") as f:
                json.dump(doc, f)
            changed.append(rid)
        newstate[rid] = len(ev)
    if a.commit:
        os.makedirs(os.path.dirname(STATE), exist_ok=True)
        with open(STATE, "w") as f:
            json.dump(newstate, f, indent=1, sort_keys=True)
    print("\n".join(changed) if changed else "(nothing new to mirror)")

if __name__ == "__main__":
    main()
