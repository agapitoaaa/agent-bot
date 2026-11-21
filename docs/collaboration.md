# Collaboration: personalities, conversation, learning

**Personalities**: each agent has a named persona (voice, blind spot, how they disagree) so discussions have real friction. Deliverables stay professional; personality shows in discussions.

**Conversation** (agents can't message each other; the orchestrator relays through files):
- Handoff Q&A: an agent can end its reply with `QUESTIONS FOR <agent>:`; the orchestrator relays and returns answers.
- `/huddle <topic>`: round-table in `runs/<id>/discussions/`, max 2 rounds, ends in a decision or an escalation to the human.

**Learning from mistakes**:
- `/retro <what happened>` runs automatically when a step fails, QA says "fix first", or you report a problem. Blameless: accounts -> root cause and plan -> fix -> verify -> lessons.
- Lessons persist in `memory/<agent>.md` (personal) and `memory/team.md` (shared rules). Agents read both at the start of every task. This file-based memory is the only thing that carries across runs.

Limits: personalities and learning are prompt-driven. They only change behavior through what gets written to memory and read next time, so keep memory short and reviewed (you can edit any memory file).
