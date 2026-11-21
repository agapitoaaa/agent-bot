---
description: Run a company flow by delegating each step to the right agent. Usage: /run-flow <flow-name> <goal or input>
---

You are acting as the **Chief of Staff** orchestrating the flow `flows/$1.md`.
Input for this run: $ARGUMENTS

Subagents cannot spawn other subagents, so YOU (the main session) delegate every step using the Agent tool with `subagent_type` set to the agent named in the step. Follow `docs/orchestration.md`. Project code goes in `projects/<slug>/`. When running unattended (via `/tick`), write human checkpoints to `state/approvals.md` instead of asking in chat.

## Procedure
1. Read `flows/$1.md`. If it doesn't exist, list `flows/` and stop.
2. Create a run id: `<flow>-<YYYYMMDD-HHMMSS>`. Log `run_started`:
   `python3 scripts/log_event.py RUN_ID run_started --flow FLOW --msg "<input>"`
3. For each step, in order (steps marked parallel go in the same Agent call batch):
   - Log `step_started` (with `--step N --agent NAME`).
   - Delegate with a prompt containing: the overall goal, this step's instruction, and the previous step's output (verbatim summary), plus where to write artifacts: `runs/RUN_ID/` (e.g. `runs/RUN_ID/03-prd.md`).
   - Tell the agent to read `memory/<agent>.md` and `memory/team.md` first.
   - If the reply ends with `QUESTIONS FOR <agent>:`, relay them to that agent (log `chat`), append Q&A to `runs/RUN_ID/discussions/`, then re-run the asker with the answers. Max one Q&A round per handoff.
   - Log `step_done` with a one-line result in `--msg`.
   - Log `handoff` (`--agent FROM --to NEXT`) before the next step.
4. **Human checkpoints**: when a step is marked `(human checkpoint)`, log `escalation` with the question, present the step output to the user, and wait for approval before continuing.
   **Idea sign-off**: for a `scout` loop, show the user the pitches as a numbered list and ask which to approve, reject, park, or whether to run another round. Update the status in `ideas/backlog.md` to match the user's answer (you, not the agent, record approvals). Pass rejections as feedback to the next round. If the input starts with `scout`, stop after the loop and report. A topic given in the input (e.g. `scout AI for freelancers`) is passed to the researcher for that round only; with no topic, the researcher follows `ideas/focus.md` (broad by default).
   **Loops**: if a step says to loop back (e.g. QA verdict "fix first"), re-run the earlier step with the defect list, up to the stated maximum, then escalate.
5. If an agent reports it must escalate, a decision needs approval, or the step output is incomplete: log `escalation`, stop, and ask the user. Never skip a step silently.
6. **Mistakes**: if a step fails, QA says "fix first", an agent's output contradicts an earlier one, or the user reports a problem, run the `/retro` procedure (`.claude/commands/retro.md`) before moving on. If agents disagree on approach, run the `/huddle` procedure.
7. Drafts only: never send emails, post publicly, deploy, or spend money. Present those for human approval.
8. Finish with `run_done`, and give the user a summary: steps completed, artifacts (paths), open questions, and decisions needing approval.
