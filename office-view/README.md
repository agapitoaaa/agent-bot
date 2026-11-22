# Office view

A visual of sprites moving around a virtual office, one per agent.

Rough plan:
- Each agent in `.claude/agents` = a character with a desk.
- Each flow in `flows/` = movement/handoffs between desks.
- Stack TBD (likely plain HTML canvas or Phaser). Events come from a simple JSON log of agent activity.

## Status
- `style-preview.html`: side-by-side demo of two candidate styles (pixel vs isometric), driven by a scripted run. Published as an artifact.
- TODO when going live: replace the scripted run with a reader for `runs/*.jsonl` (events in `docs/orchestration.md`). Artifacts can't read the repo, so live mode needs the logs published alongside the page or a small local server. **Remind the user about this when we move to live.**

## Decision
Style chosen: **isometric flat color, with slimes as the employees** (anime theme). `office.html` is the working view; `style-preview.html` is the earlier pixel-vs-isometric comparison, kept for reference.

Slime roster (matches `.claude/agents`): Nova (explorer cap), Marlowe (round glasses), Sage (beret), Pixel (headphones), Atlas (hard hat), Vex (goggles), Anchor (captain hat), Quill (feather quill). You are the crowned slime at the Approvals desk.

When adding an agent: add a cast entry (desk, body color, accessory) in `office.html` and an `office:` line in its agent file.

## Live mode (built)
`office.html` can play real run logs: sample, file, URL, or live polling. See `docs/orchestration.md`. Remaining for the laptop session: serve the repo locally and point the view at `runs/<run_id>.jsonl`. A cloud-published page can't read the repo.

## Control room (office.html)
The page is the human's single place to run the pipeline: Pipeline status, Approvals (with full documents), Actions (run next step, scout now, message the team, pause), Research focus. All state lives in the artifact database (`approvals`, `commands`, `settings/focus`, `settings/autonomy`, `status/pipeline`); Claude (or the tick) reads commands/settings and writes status. See `docs/autonomy.md`.

## Trading department
Ledger (`trader`) has a corner of the office: two-monitor desk, a market board on the wall, and a green rug. Events `trade_opened`, `trade_closed`, `risk_block` and `halt` animate him (bubbles, alerts). Paper only; no real trades exist.
