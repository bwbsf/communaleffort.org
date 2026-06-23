---
plan_id: 2026-06-23-11-31-01_bootstrap-agents-framework
title: Bootstrap Agents Framework
summary: Integrate the agents framework submodule into this host repository.
status: past
created_at: 2026-06-23-11-31-01
---

# Bootstrap Agents Framework

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Confirm integration source.
  - [x] 1.1 Read submodule bootstrap guidance.
    - [x] 1.1.1 Read `./agents/README.md`.
    - [x] 1.1.2 Read `./agents/playbooks/how_to_bootstrap_framework_submodule_into_host_repo.md`.
    - [x] 1.1.3 Read `./agents/RULES.md`.
- [x] 2. Bootstrap host operational structure.
  - [x] 2.1 Create required host operational directories.
    - [x] 2.1.1 Create `./plans/future/`, `./plans/current/`, and `./plans/past/`.
    - [x] 2.1.2 Create `./journal/` and `./kanban/`.
    - [x] 2.1.3 Create `./downtime/reports/pending/` and `./downtime/reports/reviewed/`.
  - [x] 2.2 Create host runtime shims.
    - [x] 2.2.1 Create `./AGENTS.md` pointing to `./agents/RULES.md`.
    - [x] 2.2.2 Create runtime-specific shims pointing to `./agents/RULES.md`.
  - [x] 2.3 Copy missing host-managed framework directories.
    - [x] 2.3.1 Copy `./agents/playbooks/` to `./playbooks/`.
    - [x] 2.3.2 Copy `./agents/references/` to `./references/`.
    - [x] 2.3.3 Copy `./agents/templates/` to `./templates/`.
    - [x] 2.3.4 Copy `./agents/scripts/` to `./scripts/`.
- [x] 3. Verify host integration.
  - [x] 3.1 Regenerate and check plan indexes.
    - [x] 3.1.1 Run `python3 agents/scripts/regenerate_plan_indexes.py --repo-root .`.
    - [x] 3.1.2 Run `python3 agents/scripts/regenerate_plan_indexes.py --check --repo-root .`.
  - [x] 3.2 Review repository state.
    - [x] 3.2.1 Review `git status`.
    - [x] 3.2.2 Review relevant diffs.
- [x] 4. Document integration.
  - [x] 4.1 Update host documentation.
    - [x] 4.1.1 Add README agent framework integration notes.
