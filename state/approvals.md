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
- Status: open
- Asked: 2026-11-22T09:09:09Z
- Summary: 5 pitches in ideas/backlog.md (P1-P5). Recommended: P1 Agent-file Linter. Evidence is mostly vendor blogs and trade press; demand is unverified for every idea. Run: scout-20261122-090747.
- Decision:
