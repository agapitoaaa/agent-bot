#!/usr/bin/env python3
"""Append one event to runs/<run_id>.jsonl. Used by /run-flow; consumed by the office view.

usage: log_event.py RUN_ID TYPE [--flow F] [--step N] [--agent A] [--to B] [--msg TEXT]
TYPE: run_started | step_started | handoff | step_done | escalation | run_done
"""
import argparse, json, pathlib, datetime

p = argparse.ArgumentParser()
p.add_argument("run_id"); p.add_argument("type")
p.add_argument("--flow"); p.add_argument("--step", type=int)
p.add_argument("--agent"); p.add_argument("--to"); p.add_argument("--msg", default="")
a = p.parse_args()

ev = {"ts": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
      "run_id": a.run_id, "type": a.type}
for k in ("flow", "step", "agent", "to"):
    v = getattr(a, k)
    if v is not None:
        ev[k] = v
if a.msg:
    ev["msg"] = a.msg

root = pathlib.Path(__file__).resolve().parent.parent / "runs"
root.mkdir(exist_ok=True)
with open(root / f"{a.run_id}.jsonl", "a") as f:
    f.write(json.dumps(ev) + "\n")
