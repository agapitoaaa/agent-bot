# Live office

Two ways to watch real runs, both reading the real `runs/*.jsonl` logs written by `scripts/log_event.py`.

## 1. In the claude.ai page (cloud)
- The office artifact subscribes to its database collection `runlogs` (one doc per run: `{run_id, events[], lines, updatedAt}`).
- Source "Live": pick a run (or follow the newest); older events catch up quietly, the latest few animate; new events animate as they arrive.
- A cloud page cannot read the repo, so **Claude mirrors the logs**: `/mirror` (scripts/export_runs.py + ArtifactData) is run by the orchestrator after stages and at the end of every tick. So it is near-live, not instant. `state/mirrored.json` records how many events of each run are already mirrored.
- The page opens in Live automatically when runs exist, unless you chose another source.

## 2. On your laptop (real time, no mirroring)
```
git pull
python3 scripts/serve_office.py          # localhost only, read-only
```
Open http://localhost:8000/office-view/office.html. The page detects localhost, lists `runs/*.jsonl` from `/api/runs`, polls every 2 s, follows the newest run, and animates new events. It reads the files straight from disk, so anything that logs an event shows up within about two seconds. (Approvals and controls still need the claude.ai page, which holds the database.)

## What shows up
Only events that something logged. The orchestrator logs run/step/handoff/escalation events (`docs/orchestration.md`); the more consistently agents and commands log, the richer the live view. Subagents' internal tool calls are not logged.

## Caveats
Mirroring costs a tool call per sync; the cloud page lags by that. The laptop server serves the repo root over HTTP on 127.0.0.1 only; do not expose it to a network.
