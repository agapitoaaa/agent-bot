# Autonomy

A scheduled task runs `/tick` every few hours in a fresh session. Each tick does one bounded step and stops at human checkpoints.

State machine: `idle -> scouting -> [idea approval] -> research brief + plan -> [plan approval] -> design -> development -> testing -> release prep -> [deploy approval] -> handoff -> idle`

Your only jobs: answer requests in `state/approvals.md` (edit the file on GitHub, or tell Claude in chat).
Safety: no deploy/publish/send/spend without an explicit answered approval; bounded work per tick; failures escalate to you.
Limits: fresh sessions don't see chat history, so everything important lives in files; the schedule runs only while the scheduled task is enabled.
Stop it: disable or delete the scheduled task.

Steering research: `ideas/focus.md` says `broad` by default. Put specific topics there (or tell Claude) to narrow the researcher; set it back to `broad` to clear.
