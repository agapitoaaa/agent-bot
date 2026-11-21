# agent-bot

A workshop for building personal AI agent bots: skills, subagents, instructions, and flows.
A later phase adds an "office view" that animates sprites for each agent working in a virtual workplace.

## Layout
- `.claude/skills/<name>/SKILL.md`: reusable skills (frontmatter `name`, `description`, then instructions)
- `.claude/agents/<name>.md`: subagents (frontmatter `name`, `description`, `tools`, `model`)
- `.claude/commands/<name>.md`: slash commands
- `ideas/backlog.md`: researcher idea pitches and their sign-off status
- `flows/<name>.md`: multi-step workflows that chain agents and skills (see `flows/README.md`)
- `docs/`: design notes and decisions; `docs/team.md` lists the agents
- `office-view/`: the future sprite-based office visualization (see `office-view/README.md`)

- `memory/`: per-agent lessons + `team.md` shared rules; `docs/collaboration.md`: personas, huddles, retros
- `state/`: pipeline state + `approvals.md` inbox (autonomy, see `docs/autonomy.md`); `projects/`: built products; `/tick` runs one autonomous step
- `scripts/`: helpers (`log_event.py` writes run events); `runs/`: flow run logs; `docs/orchestration.md`: how `/run-flow` works

## Conventions
- One skill/agent per file or folder, with a specific `description` so it triggers correctly.
- Each agent owns one pipeline stage. Flows define the handoffs; the main session orchestrates.
- Every agent and flow should declare an `office:` stage/desk in its docs, so the office view can map it to a sprite later.
