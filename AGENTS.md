# AGENTS Instructions

Read `./agents/RULES.md` in its entirety before doing anything in this repository. Follow all instructions in `./agents/RULES.md` as though they are written directly in this file. Do not proceed if you have not read and understood `./agents/RULES.md`.

Framework resolution from the host project root:
- Use host-managed `./playbooks/`, `./references/`, `./templates/`, and `./scripts/` when present.
- Fall back to `./agents/playbooks/`, `./agents/references/`, `./agents/templates/`, and `./agents/scripts/` when host copies are missing.
- For host-owned plans, run `python3 agents/scripts/regenerate_plan_indexes.py --repo-root .`.

Host integration notes:
- This repository consumes `cjtrowbridge/agents` as a git submodule at `./agents`.
- Canonical agent policy lives in `./agents/RULES.md`.
- Runtime shim files (`AGENTS.md`, `CODEX.md`, `CLAUDE.md`, `GEMINI.md`, and `OPENCODE.md`) direct agents to that policy.
- Host-managed framework working copies live in `./playbooks/`, `./references/`, `./templates/`, and `./scripts/`.
- Host-owned operational artifacts live in `./plans/`, `./journal/`, `./kanban/`, and `./downtime/reports/`.
