---
description: Blameless post-mortem when something went wrong; agents discuss, plan a fix, and record lessons. Usage: /retro <what happened>
---

Run a blameless retro on: $ARGUMENTS

1. **Facts**: gather what actually happened (run logs, outputs, test reports, the user's complaint). Create `runs/<RUN_ID>/discussions/<NN>-retro-<slug>.md` with a "What happened" section of facts and evidence only, no blame. Log `mistake` (`--agent` = whoever's output was wrong, if known).
2. **Round 1, accounts**: delegate to each involved agent (plus whoever caught it), one at a time. Each reads the transcript and their memory, then appends: what I did and why, what I'd do differently, what I needed that I didn't have.
3. **Round 2, root cause and plan**: delegate again, one at a time. Each responds to others by name and proposes root cause(s) and fix steps. Log a `chat` per turn.
4. **Synthesize**: root cause (process, not person), fix plan with owner per step, and 1-3 preventive rules. If the fix touches deploy, spend, scope or anything outward-facing, get the user's approval first.
5. **Fix**: have the owner execute the plan, then have QA (or the agent who caught it) verify. If it fails verification, repeat once, then escalate to the user.
6. **Learn**: ask each involved agent to append a lesson to their own `memory/<agent>.md`. You append team-wide rules to `memory/team.md`. Log a `lesson` event per lesson (`--agent`, `--msg` = the rule).
7. Log `retro_done`. Tell the user: what went wrong, the fix, the new rules.
