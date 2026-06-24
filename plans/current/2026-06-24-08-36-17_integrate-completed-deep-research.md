---
plan_id: 2026-06-24-08-36-17_integrate-completed-deep-research
title: Integrate Completed Deep Research
summary: Update integration governance to require commits after each report, commit the SF integration, then integrate and commit Reno, Fly Ranch, and South Bay one at a time.
status: current
created_at: 2026-06-24-08-36-17
---

# Integrate Completed Deep Research

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Update integration governance.
  - [x] 1.1 Update `playbooks/how_to_integrate_deep_research_results.md` to require a task-scoped commit after every completed research integration.
  - [x] 1.2 Document that agents must stop before the next report if verification fails.
- [x] 2. Commit already-completed SF integration.
  - [x] 2.1 Verify SF chapter opportunities and archive state.
  - [x] 2.2 Commit SF integration and playbook governance update.
- [x] 3. Integrate Reno report.
  - [x] 3.1 Import Reno opportunities into `chapters/north-america/reno/index.md`.
  - [x] 3.2 Move Reno report to `research/archive/`.
  - [x] 3.3 Mark Reno targets integrated in `research/status.yml`.
  - [x] 3.4 Verify prompt generation and chapter YAML.
  - [x] 3.5 Commit Reno integration.
- [x] 4. Integrate Fly Ranch report.
  - [x] 4.1 Import Fly Ranch opportunities into `chapters/north-america/fly-ranch/index.md`.
  - [x] 4.2 Move Fly Ranch report to `research/archive/`.
  - [x] 4.3 Mark Fly Ranch targets integrated in `research/status.yml`.
  - [x] 4.4 Verify prompt generation and chapter YAML.
  - [x] 4.5 Commit Fly Ranch integration.
- [ ] 5. Integrate South Bay report.
  - [ ] 5.1 Import South Bay opportunities into `chapters/north-america/south-bay/index.md`.
  - [ ] 5.2 Move South Bay report to `research/archive/`.
  - [ ] 5.3 Mark South Bay imported targets integrated while preserving `no-good-leads` for mutual aid.
  - [ ] 5.4 Verify prompt generation and chapter YAML.
  - [ ] 5.5 Commit South Bay integration.
- [ ] 6. Close the plan.
  - [ ] 6.1 Append journal checkpoints for each integration.
  - [ ] 6.2 Archive this plan and regenerate indexes.
  - [ ] 6.3 Verify final status and report commit hashes.
