# Team

The orchestrator is the main Claude session (acting as Chief of Staff via `/run-flow`); it has no agent file.

| Stage | Agent | Role |
|---|---|---|
| research | researcher | Researcher (stage 1). Use first: market, competitor, user-need and feasibility research for a product idea. |
| planning | planner | Planner (stage 2). Use after research to produce the PRD, scope, milestones, and task breakdown. |
| design | designer | Designer (stage 3). Use after planning for user flows, screen specs, and visual style (UX + UI). |
| development | backend-engineer | Backend Engineer (stage 4). Use to build APIs, data and logic per the plan. |
| development | frontend-engineer | Frontend Engineer (stage 4). Use to build UI per the design spec. |
| testing | qa-engineer | QA Engineer (stage 5). Use after development to test against acceptance criteria and review code quality and security basics. |
| execution | release-engineer | Release Engineer (stage 6). Use after QA passes to build, package, and prepare deployment. Never deploys without human approval. |
| handoff | handoff-writer | Handoff Writer (stage 7). Use last to write the product handoff package: README, usage, architecture, known issues, next steps. |

The larger 38-role company (executives, marketing, sales, finance, legal...) was removed to keep this lean; it lives in git history (commit aa7c0f8) if we want to bring back departments.
