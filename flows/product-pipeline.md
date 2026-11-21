# Flow: product pipeline

Continuous idea scouting -> human sign-off -> shipped product -> handoff.

**Trigger**: the user starts a run, optionally with a focus area (e.g. "AI tools for freelancers"), or the user approves an idea from the backlog.

## Steps
1. **Scout loop** `researcher` (mode: scout) -> `ideas/focus.md` (default: broad) + `ideas/backlog.md` -> 3-5 ranked idea pitches
   - (**human checkpoint: idea sign-off**) The user picks one idea to approve, rejects/parks others, or asks for another round. Repeat scouting (with feedback) until an idea is approved. Nothing proceeds without an approval.
2. `researcher` (mode: brief) -> the approved idea -> `research.md`
3. `planner` -> `research.md` -> `plan.md`  (**human checkpoint: approve plan**)
4. `designer` -> `plan.md` -> `design.md`
5. (parallel) `frontend-engineer` + `backend-engineer` -> `plan.md`, `design.md` -> code + `dev-*.md`
6. `qa-engineer` -> code + acceptance criteria -> `test-report.md`  (if verdict is "fix first": loop to step 5, max 2 times, then escalate)
7. `release-engineer` -> passing build -> `release.md`  (**human checkpoint: approve before any real deploy**)
8. `handoff-writer` -> everything -> `handoff.md`, README

## Done when
Handoff package delivered and the user has the product, docs, and open issues list.

Scouting can also run on its own to just refill the backlog: `/run-flow product-pipeline scout <focus>` stops after step 1.

office: flow=product-pipeline (agents walk desk-to-desk in stage order)
