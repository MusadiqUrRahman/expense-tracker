# CLAUDE.md - Quick Notes

## What is CLAUDE.md?
- A markdown file that gives **instructions to Claude Code**
- Claude reads it **automatically** at the start of every conversation
- Think of it as a **rulebook** for Claude in your project

## Where does it go?
- **Project root** (`expense-tracker/CLAUDE.md`) — most common, shared with team
- **Home directory** (`~/.claude/CLAUDE.md`) — personal, applies to ALL projects
- **Subdirectory** (`database/CLAUDE.md`) — applies only to that folder

## What to write inside?
- Project setup commands (how to run, test, build)
- Coding rules (e.g., "use raw SQL, no ORM")
- Architecture overview (how files connect)
- Things to avoid (e.g., "don't add new dependencies")

## CLAUDE.md vs .claude/ folder
- `CLAUDE.md` = YOUR instructions to Claude (you write it)
- `.claude/` folder = Claude's internal data (plans, memory — Claude writes it)
- They are **two completely different things**

## Key Points
- No special setup needed — just create the file and Claude reads it
- Keep it short and focused — Claude reads it every time
- Update it as your project grows
- Commit it to git so your team benefits too
