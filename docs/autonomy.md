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

## Control room
The office page also holds Actions (queue `run_next`, `scout`, or a `note` for the team; pause/resume autonomy) and Research focus. They write `commands`, `settings/autonomy` and `settings/focus` in the artifact database. Whoever runs the tick (the scheduled task once repo access is fixed, or Claude in chat) applies them and writes `status/pipeline` for the Pipeline card.

## Why answering did not start work (and the fix)
The panel only SAVES answers; nothing was listening. A chat session notices them only when it looks, and the scheduled task is marked paused (it still runs when fired manually). Fix (2026-11-24): the office page can start the scheduled task itself (connector "Claude Code Remote", tool `fire_trigger`, trigger `trig_01SFmKbvWeDb9LqiYAcXHiep`). Buttons: **Start work now**, and optional **Start automatically after I answer** (15 s after the last answer, at most once per 3 minutes; off switch in the Actions card). The first use asks for permission. Runs take the single-runner lock (`status/runner`) so two sessions do not collide (see `.claude/commands/tick.md`).
