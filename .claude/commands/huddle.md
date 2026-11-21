---
description: Convene agents to discuss a topic and reach a decision. Usage: /huddle <topic> [with agent1,agent2,...]
---

Convene a huddle on: $ARGUMENTS

You are the orchestrator; agents can't talk directly, so you relay through a shared transcript.

1. Pick participants (those named after `with`, else the 2-4 agents most affected). Create `runs/<RUN_ID>/discussions/<NN>-<topic-slug>.md` with the topic, context, and the question to settle. RUN_ID is the current run, or `huddle-<YYYYMMDD-HHMMSS>` if standalone.
2. Log: `python3 scripts/log_event.py RUN_ID huddle_started --msg "<topic>"`.
3. **Round 1**: delegate to each participant in turn (not parallel, so they can read earlier turns). Tell each: read the transcript, `memory/<agent>.md`, `memory/team.md`, append one in-persona turn. After each turn log `chat` with `--agent FROM --to NEXT --msg "<one-line gist>"`.
4. **Round 2** (only if there is disagreement): each disagreeing participant replies once to specific points. Maximum 2 rounds.
5. Synthesize at the bottom of the transcript: **Decision**, **Owner**, **Next step**, and any **Unresolved disagreement** with both positions. If unresolved, or the decision affects scope, spend, deploy or anything outward-facing, ask the user to decide.
6. Log `huddle_ended`. Summarize to the user in a few lines and link the transcript.
