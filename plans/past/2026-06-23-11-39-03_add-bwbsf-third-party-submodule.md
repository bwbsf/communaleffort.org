---
plan_id: 2026-06-23-11-39-03_add-bwbsf-third-party-submodule
title: Add BWBSF Third-Party Submodule
summary: Add the BWBSF website repository under the host repository's third-party directory.
status: past
created_at: 2026-06-23-11-39-03
---

# Add BWBSF Third-Party Submodule

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Confirm requested dependency location.
  - [x] 1.1 Use `./third_party/` for the external repository.
    - [x] 1.1.1 Target submodule path `./third_party/bwbsf.org`.
- [x] 2. Add repository as a submodule.
  - [x] 2.1 Add `https://github.com/bwbsf/bwbsf.org.git`.
    - [x] 2.1.1 Run `git submodule add https://github.com/bwbsf/bwbsf.org.git third_party/bwbsf.org`.
- [x] 3. Verify repository state.
  - [x] 3.1 Refresh and check plan indexes.
    - [x] 3.1.1 Run `python3 agents/scripts/regenerate_plan_indexes.py --repo-root .`.
    - [x] 3.1.2 Run `python3 agents/scripts/regenerate_plan_indexes.py --check --repo-root .`.
  - [x] 3.2 Review resulting git state.
    - [x] 3.2.1 Run `git status --short`.
    - [x] 3.2.2 Run `git submodule status`.
