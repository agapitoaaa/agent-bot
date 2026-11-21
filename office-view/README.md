# Office view (planned)

A visual of sprites moving around a virtual office, one per agent.

Rough plan:
- Each agent in `.claude/agents` = a character with a desk.
- Each flow in `flows/` = movement/handoffs between desks.
- Stack TBD (likely plain HTML canvas or Phaser). Events come from a simple JSON log of agent activity.
