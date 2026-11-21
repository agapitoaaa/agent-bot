# Going live: laptop session checklist

Goal: run the pipeline and the slime office on the laptop with real events instead of the scripted demo.

## 1. Environment
- [ ] Clone the repo, check out `claude/fervent-albattani-ozphm8`
- [ ] Install Claude Code CLI and log in
- [ ] Python 3 available (for `scripts/log_event.py`)
- [ ] Node (optional, only if we add a small local server)

## 2. Real run first
- [ ] Review what the scheduled `/tick` did so far (`state/`, `ideas/backlog.md`, `runs/`, git log)
- [ ] Answer any open requests in `state/approvals.md`
- [ ] Run `/run-flow product-pipeline scout` locally to generate real `runs/*.jsonl` events

## 3. Wire the office view
- [ ] Local server that serves `office-view/office.html` plus the latest `runs/*.jsonl` (or a `/events` endpoint)
- [ ] Replace the scripted `Sim` with an event reader (map events to animations per `docs/orchestration.md`)
- [ ] Live mode: poll or tail the newest log; replay mode: pick a past run
- [ ] Add an approvals panel reading `state/approvals.md`

## 4. Decide
- [ ] Keep the scheduled cloud ticks, run locally, or both
- [ ] Merge the working branch to `main` (needs a PR)
- [ ] Scout focus (`ideas/focus.md`) and cadence of ticks
