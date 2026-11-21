# Orchestration

## How a flow runs
`/run-flow <flow> <input>` makes the main Claude session act as Chief of Staff:
read `flows/<flow>.md` -> delegate each step to the named subagent -> pass outputs forward -> log events.

Why the main session? Subagents cannot launch other subagents, so a CEO agent can't delegate to its reports. Delegation is flat: the orchestrator calls each employee directly, following the flow (and the org chart for escalation).

## Artifacts
Each run writes to `runs/<run_id>/` (step outputs) and `runs/<run_id>.jsonl` (events).

## Event log (feeds the office view)
One JSON object per line:
`{"ts","run_id","type","flow","step","agent","to","msg"}`

| type | meaning | office view animation |
|---|---|---|
| run_started | flow begins | everyone idle at desks |
| step_started | agent begins work | agent sprite "working" at desk |
| handoff | work passes `agent` -> `to` | sprite walks to `to`'s desk |
| step_done | agent finished | sprite returns / idle |
| escalation | needs human or manager | sprite goes to manager / alert icon |
| run_done | flow complete | celebrate |

Write events with `python3 scripts/log_event.py` only.

## Guardrails
- Drafts only for anything outward-facing (email, social, deploy, spend, legal).
- Escalate instead of guessing.
