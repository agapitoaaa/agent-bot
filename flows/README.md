# Flows

A flow is a named, multi-step process that chains agents and skills.

Format for `flows/<name>.md`:
- **Trigger**: what starts it
- **Steps**: ordered list of `agent/skill -> input -> output`
- **Handoffs**: what passes between steps
- **Done when**: completion criteria

Flows are the source of truth the office view will animate (agents walking between desks as work is handed off).
