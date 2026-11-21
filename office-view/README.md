# Office view (planned)

A visual of sprites moving around a virtual office, one per agent.

Rough plan:
- Each agent in `.claude/agents` = a character with a desk.
- Each flow in `flows/` = movement/handoffs between desks.
- Stack TBD (likely plain HTML canvas or Phaser). Events come from a simple JSON log of agent activity.

## Status
- `style-preview.html`: side-by-side demo of two candidate styles (pixel vs isometric), driven by a scripted run. Published as an artifact.
- TODO when going live: replace the scripted run with a reader for `runs/*.jsonl` (events in `docs/orchestration.md`). Artifacts can't read the repo, so live mode needs the logs published alongside the page or a small local server. **Remind the user about this when we move to live.**
