---
plan_id: 2026-06-23-11-37-03_keep-readme-human-oriented
title: Keep README Human-Oriented
summary: Move agent integration details out of the public README and into agent-facing instructions.
status: past
created_at: 2026-06-23-11-37-03
---

# Keep README Human-Oriented

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Confirm documentation target.
  - [x] 1.1 Treat `README.md` as human-facing project documentation.
    - [x] 1.1.1 Preserve the human project summary in `README.md`.
- [x] 2. Move agent-specific details.
  - [x] 2.1 Remove agent framework section from `README.md`.
    - [x] 2.1.1 Delete the `Agent Framework` section.
  - [x] 2.2 Add integration details to `AGENTS.md`.
    - [x] 2.2.1 Document submodule, shim, host-managed, and operational paths.
- [x] 3. Verify cleanup.
  - [x] 3.1 Regenerate plan indexes.
    - [x] 3.1.1 Run `python3 agents/scripts/regenerate_plan_indexes.py --repo-root .`.
    - [x] 3.1.2 Run `python3 agents/scripts/regenerate_plan_indexes.py --check --repo-root .`.
  - [x] 3.2 Review repository state.
    - [x] 3.2.1 Review `git status`.
    - [x] 3.2.2 Review relevant diffs.
