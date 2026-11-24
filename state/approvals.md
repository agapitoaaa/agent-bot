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
- Status: answered
- Asked: 2026-11-22T09:15:04Z
- Summary: Generic P2 is served by free tools (ccusage, agentsight) and vendor features. Options: narrow (per-flow-stage cost + waste detection, recommended), internal tool only, or go back to the idea list. Full brief: runs/product-pipeline-20261122-091241/research.md
- Decision: approve narrow (per-flow-stage cost for multi-agent workflows + waste detection) (answered 2026-11-24T15:59:57Z via office panel)

### A3: plan | Plan: Ledger, the paper-trading agent
- Status: answered
- Asked: 2026-11-22T09:19:22Z
- Summary: Plan for a paper-trading-only trader agent (docs/trader-bot-plan.md). Choose phase-1 market (us-equities recommended) and answer the questions in the note. Approval starts the foundation phase only; real money is out of scope without a separate approval.
- Decision: approve; market = both (US stocks + crypto); no note given (answered 2026-11-22T09:28:18Z via office panel)

### A4: plan | Ledger: path to real money, for the Philippines
- Status: answered
- Asked: 2026-11-22T09:35:57Z
- Summary: Readiness roadmap (docs/trader-live-readiness.md) and platform research (docs/trader-platforms.md). Choose: assisted live (recommended), API live later, or paper only. No live trading happens in any option without separate approvals.
- Decision: approve assisted (paper trading now, assisted live later: human places any real orders; no live API keys) (answered 2026-11-24T16:00:01Z via office panel)

### A5: plan | Ledger: what he studies and tests first
- Status: answered
- Asked: 2026-11-22T11:13:57Z
- Summary: Curriculum, strategy catalog and source catalog (trading/knowledge/). Recommended: benchmark plus one trend experiment (max 3 parameter sets), with QA challenge. Approving only lets Ledger write pre-registered hypotheses; nothing is coded or run.
- Decision: approve baseline-trend (benchmark + one trend experiment, max 3 parameter sets, QA challenge before promotion) (answered 2026-11-24T16:00:15Z via office panel)


### A6: plan | Plan: agent-spend-lens (narrow: per-flow-stage cost + waste flags)
- Status: answered
- Asked: 2026-11-24T16:20:00Z
- Summary: Plan at runs/product-pipeline-20261122-091241/plan.md. Local read-only Python CLI + static HTML report attributing estimated USD cost per flow step from runs/*.jsonl joined with Claude Code session logs; explainable waste flags. Open decisions: (1) Python stdlib only (recommended) vs Node; (2) location in this repo vs separate; (3) is usefulness for our own flows enough given unproven demand; (4) confirm attribution policy (step time window, unmatched = unattributed); (5) publishing stays a separate human decision. Approve = proceed to design and build M0 (schema check) first.
- Decision: park (answered via office panel)

### A7: idea | Game project: pick a game idea (PC, Godot or Unity)
- Status: open
- Asked: 2026-11-24T16:22:43Z
- Summary: Nova's Steam scout (tags idle, loot, ARPG, desktop companion, adventure): five game pitches G1-G5 in ideas/backlog.md (Game track). Recommended: G1 Slime Strip, with G4 Slime Pal as a cheap first proof of the window technique.
- Decision:

