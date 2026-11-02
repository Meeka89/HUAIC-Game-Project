# Shared instructions for AI agents

Read [README.md](README.md), [confirmed decisions](docs/DECISIONS.md), and the project documents relevant to your task before changing anything. Use repository documents as shared context; do not assume access to members' private AI chats.

- Distinguish agreed decisions, proposed ideas, open questions, and action items. Suggestions and AI summaries are not approvals. Never invent agreement, owners, deadlines, or verification results.
- Work on one agreed task at a time. Check existing tasks and implementations first, and keep changes focused. Larger features need agreement before implementation.
- Identify dependencies and integration points with existing work before adding or replacing an implementation. Coordinate changes that affect another contributor's work.
- Do not silently change architecture, engine, scope, dependencies, or design. Propose changes and obtain agreement before implementing them; record approved decisions in the shared documents.
- Read [GAME_DESIGN.md](docs/GAME_DESIGN.md) and [PROTOTYPE.md](docs/PROTOTYPE.md) for current scope. The fantasy college-town concept is the leading proposal; the room, movement, and NPC conversation prototype is confirmed. The engine is undecided; Godot is only a candidate. Do not invent engine-specific setup, run, export, or test commands. Documentation updates do not authorize game implementation or engine selection.
- Verify changes with checks appropriate to the work. For documentation, check links and consistency; for code or assets, use the agreed checks once available. Never claim tests or playtests ran when they did not.
- Update relevant documentation when behavior changes. In your handoff, summarize changes, verification actually performed, and outstanding concerns.
- Keep secrets, private information, raw meeting recordings, and raw transcripts out of the repository. Review summaries for consent, accuracy, and unnecessary personal information before proposing them for inclusion.
- Preserve existing work and follow [CONTRIBUTING.md](CONTRIBUTING.md). Do not add integrations, automation, or dependencies without an agreed need.

Some AI tools do not automatically read `AGENTS.md`. Contributors using Codex, Claude Code, or other tools should explicitly tell their tool to read this file and the relevant shared documents before starting.
