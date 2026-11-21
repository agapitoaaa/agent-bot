# Flow: product pipeline

End-to-end: idea -> shipped product -> handoff.

**Trigger**: a product idea or goal from the user.

## Steps
1. `researcher` -> idea -> `research.md`
2. `planner` -> `research.md` -> `plan.md`  (**human checkpoint**: approve plan)
3. `designer` -> `plan.md` -> `design.md`
4. (parallel) `frontend-engineer` + `backend-engineer` -> `plan.md`, `design.md` -> code + `dev-*.md`
5. `qa-engineer` -> code + acceptance criteria -> `test-report.md`  (if verdict is "fix first": loop to step 4, max 2 times, then escalate)
6. `release-engineer` -> passing build -> `release.md`  (**human checkpoint**: approve before any real deploy)
7. `handoff-writer` -> everything -> `handoff.md`, README

## Done when
Handoff package delivered and the user has the product, docs, and open issues list.

office: flow=product-pipeline (agents walk desk-to-desk in stage order)
