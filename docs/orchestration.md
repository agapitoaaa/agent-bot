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
| chat | `agent` says something to `to` | speech bubble between sprites |
| huddle_started / huddle_ended | agents gather to discuss | sprites walk to a meeting table |
| mistake | something went wrong | alert icon over `agent` |
| lesson | an agent learned a rule | lightbulb over `agent`; `msg` is the rule |
| retro_done | retro finished | sprites return to desks |

Write events with `python3 scripts/log_event.py` only.

## Guardrails
- Drafts only for anything outward-facing (email, social, deploy, spend, legal).
- Escalate instead of guessing.

## Event conventions the office view relies on
- `agent` / `to`: use the real agent names (`frontend-engineer`, `qa-engineer`, ...) or `you`. The view maps them to slimes.
- `escalation` (agent + msg): the agent walks to the Approvals desk and waits; You gets a `?`. It clears on the next `step_started`, `handoff`, or `run_done`. Log it for every human checkpoint (idea, plan, deploy sign-off).
- `huddle_started` (`--agent` and `--to` = first two participants): those agents go to the meeting table. Anyone who then `chat`s joins the table. `huddle_ended` or `retro_done` sends everyone back.
- `mistake`, `lesson` (agent + msg): alert / lightbulb over that agent with the message as a bubble.
- `handoff` (agent -> to): sender walks a paper to the receiver. The receiver starts working only on its own `step_started`.
- Events with no known agent still show in the feed.

## Playing logs in the office view
`office-view/office.html` -> Source: Run log. Options: sample run, open a `.jsonl` file, or a URL (add Live to poll every 3s for appended events). A URL must allow CORS; the simplest live setup is a local server serving the repo (e.g. `python3 -m http.server` in the repo root, then `http://localhost:8000/runs/<run_id>.jsonl`). `office-view/samples/sample-run.jsonl` is a full example made with `scripts/log_event.py`.
