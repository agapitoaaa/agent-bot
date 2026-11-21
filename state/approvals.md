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
