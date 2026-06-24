---
plan_id: 2026-06-24-08-22-06_deep-research-archive-folder
title: Deep Research Archive Folder
summary: Add an archive folder and workflow rules for moving completed deep-research reports after integration while preserving status tracking.
status: past
created_at: 2026-06-24-08-22-06
---

# Deep Research Archive Folder

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Add archive directory documentation.
  - [x] 1.1 Create `research/archive/README.md`.
  - [x] 1.2 Explain that reports move from `research/completed/` to `research/archive/` after integration.
  - [x] 1.3 Explain that archived reports remain committed source artifacts.
- [x] 2. Update integration workflow rules.
  - [x] 2.1 Update `research/README.md` with completed-to-archive lifecycle.
  - [x] 2.2 Update `playbooks/how_to_integrate_deep_research_results.md` with archive steps.
  - [x] 2.3 Update `docs/site-structure.md` with archive folder semantics.
  - [x] 2.4 Update `AGENTS.md` with archive preservation standard.
- [x] 3. Preserve tracking behavior.
  - [x] 3.1 State that `research/status.yml` must update `completed_report` after a move to archive.
  - [x] 3.2 State that `integrated` targets remain skipped by prompt generation after archival.
  - [x] 3.3 Do not move existing completed examples until they are actually integrated.
- [x] 4. Verify archive governance.
  - [x] 4.1 Confirm generated files remain ignored.
  - [x] 4.2 Confirm archive README is tracked.
  - [x] 4.3 Review git status and diff.
