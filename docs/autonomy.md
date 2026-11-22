# Autonomy

A scheduled task runs `/tick` every few hours in a fresh session. Each tick does one bounded step and stops at human checkpoints.

State machine: `idle -> scouting -> [idea approval] -> research brief + plan -> [plan approval] -> design -> development -> testing -> release prep -> [deploy approval] -> handoff -> idle`

Your only jobs: answer requests in `state/approvals.md` (edit the file on GitHub, or tell Claude in chat).
Safety: no deploy/publish/send/spend without an explicit answered approval; bounded work per tick; failures escalate to you.
Limits: fresh sessions don't see chat history, so everything important lives in files; the schedule runs only while the scheduled task is enabled.
Stop it: disable or delete the scheduled task.

Steering research: `ideas/focus.md` says `broad` by default. Put specific topics there (or tell Claude) to narrow the researcher; set it back to `broad` to clear.

## Answering from the office page
Requests are mirrored to the office artifact's database (`approvals` collection, readable/writable only by the owner and editors). The page shows them with Approve / Park / Reject / Request changes. Decisions are saved there, and the next `/tick` (or Claude in chat) copies them into `state/approvals.md` and acts, marking the doc `applied`. Doc fields: `kind, title, summary, status, asked, options[], recommended, source, decision, chosen, note, answeredAt, applied`.
