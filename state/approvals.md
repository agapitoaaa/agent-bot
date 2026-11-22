# Approvals inbox

The autonomous pipeline stops here and waits for you. To answer, set the `Decision:` line of a request to one of:
`approve` | `reject` | `park` | `changes: <what to change>`
(or just tell Claude in chat and it will record it). The next tick picks it up.

Request format (appended by `/tick`):
### A<N>: <kind: idea | plan | deploy | escalation> | <title>
- Status: open | answered
- Asked: <date>
- Summary: <few lines + path to full artifact>
- Decision:

---

### A1: idea | Scout round 1: pick an idea (or ask for another round)
- Status: answered
- Asked: 2026-11-22T09:09:09Z
- Summary: 5 pitches in ideas/backlog.md (P1-P5). Recommended: P1 Agent-file Linter. Evidence is mostly vendor blogs and trade press; demand is unverified for every idea. Run: scout-20261122-090747.
- Decision: approve P2 (answered 2026-11-22T09:10:38Z via office panel)

### A2: escalation | Research says P2 is mostly already built. How should we proceed?
- Status: open
- Asked: 2026-11-22T09:15:04Z
- Summary: Generic P2 is served by free tools (ccusage, agentsight) and vendor features. Options: narrow (per-flow-stage cost + waste detection, recommended), internal tool only, or go back to the idea list. Full brief: runs/product-pipeline-20261122-091241/research.md
- Decision:

### A3: plan | Plan: Ledger, the paper-trading agent
- Status: answered
- Asked: 2026-11-22T09:19:22Z
- Summary: Plan for a paper-trading-only trader agent (docs/trader-bot-plan.md). Choose phase-1 market (us-equities recommended) and answer the questions in the note. Approval starts the foundation phase only; real money is out of scope without a separate approval.
- Decision: approve; market = both (US stocks + crypto); no note given (answered 2026-11-22T09:28:18Z via office panel)

### A4: plan | Ledger: path to real money, for the Philippines
- Status: open
- Asked: 2026-11-22T09:35:57Z
- Summary: Readiness roadmap (docs/trader-live-readiness.md) and platform research (docs/trader-platforms.md). Choose: assisted live (recommended), API live later, or paper only. No live trading happens in any option without separate approvals.
- Decision:

