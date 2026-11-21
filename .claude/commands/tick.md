---
description: Autonomous single step of the product pipeline. Run on a schedule; does the next piece of work, stops at human approvals. Usage: /tick
---

You are the orchestrator (Chief of Staff) running ONE autonomous tick. No human is watching: never ask questions in chat; record approval requests in `state/approvals.md` instead. Be cheap: if there is nothing to do, say so and stop.

## 0. Setup
- `git pull` the current branch. Read `state/pipeline.md`, `state/approvals.md`, `ideas/backlog.md`, `memory/team.md`.
- Update `Last tick` in `state/pipeline.md` at the end.

## 1. Apply answered approvals (in this order, handle all that apply)
For each approval with a non-empty `Decision:` and Status `open`: mark it `answered`, then:
- **idea**: `approve` -> set the idea `approved` in the backlog; `reject`/`park` -> set accordingly and record any feedback for the next scout. 
- **plan / deploy**: `approve` -> continue the pipeline from that point; `changes: ...` -> re-run the producing agent with the requested changes (counts as a retry); `reject` -> mark project `stopped`, log why.
- **escalation**: follow the instruction given, then continue.

## 2. Decide the single next action (first match wins)
1. **Project in progress and not awaiting approval** -> continue it per `flows/product-pipeline.md` from the recorded Stage, following `.claude/commands/run-flow.md` (delegate to agents, log events, huddles on disagreement, retros on mistakes). Continue until the next human checkpoint or the end of the flow, or until you have done roughly one stage group this tick (research brief+plan | design | development | testing+release prep | handoff). Save Stage in `state/pipeline.md`.
2. **Idle, and an `approved` idea exists that has no project** -> start the project: slug it, set state, run the `researcher` in brief mode, then the `planner`; then open a **plan** approval request and stop.
3. **Idle, no approved idea, and fewer than 5 ideas are `proposed`/unanswered** -> run one `researcher` scout round (broad unless the backlog notes give a focus), append pitches to the backlog, and open ONE **idea** approval request listing all new pitches with a recommendation.
4. **Otherwise** (waiting on the human) -> do nothing; report what you are waiting for.

## 3. Hard rules (non-negotiable)
- Never deploy, publish, send, post, or spend. The `release-engineer` prepares only; a real deploy requires an answered `deploy` approval with `approve`, and even then run only the documented deploy steps in `release.md`.
- Never approve anything yourself, never edit another request's `Decision:`.
- Code lives in `projects/<slug>/`. Artifacts in `runs/<run_id>/`.
- Max 2 QA fix loops per project, then open an **escalation** request. If an agent or step fails twice, run a retro, open an **escalation** request, and stop.
- Budget: at most ~8 agent calls per tick. If unfinished, save state and stop; the next tick continues.
- Log events with `scripts/log_event.py` as `/run-flow` describes.

## 4. Finish
Commit all changes (state, ideas, runs, memory, projects) with a clear message and push to the current branch (retry network errors up to 4 times). End with a 3-line status: what you did, what you're waiting on, next expected action.
