---
plan_id: 2026-06-23-12-48-13_update-website-taxonomy-standard
title: Update Website Taxonomy Standard
summary: Revise the queued website hierarchy plan and agent guidance to use a continent-to-metro/region taxonomy instead of jurisdiction-first paths.
status: past
created_at: 2026-06-23-12-48-13
---

# Update Website Taxonomy Standard

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Confirm taxonomy decision.
  - [x] 1.1 Adopt a city/metro-first hierarchy after continent.
    - [x] 1.1.1 Keep country and state/province as metadata rather than URL spine.
    - [x] 1.1.2 Align the standard with the “Without Borders” framing.
- [x] 2. Update queued implementation plan.
  - [x] 2.1 Patch `plans/future/2026-06-23-12-41-07_website-hierarchy-and-content-taxonomy.md`.
    - [x] 2.1.1 Replace jurisdiction-first examples with continent-to-metro examples.
    - [x] 2.1.2 Add slug disambiguation rules.
    - [x] 2.1.3 Preserve country and state/province as data fields only.
- [x] 3. Update agent-facing standards.
  - [x] 3.1 Patch `AGENTS.md`.
    - [x] 3.1.1 Add website taxonomy decisions.
    - [x] 3.1.2 Add assumptions and expectations for future iterations.
- [x] 4. Verify and journal.
  - [x] 4.1 Update today's journal.
    - [x] 4.1.1 Log the taxonomy-standard update.
  - [x] 4.2 Refresh plan indexes.
    - [x] 4.2.1 Run `python3 agents/scripts/regenerate_plan_indexes.py --repo-root .`.
    - [x] 4.2.2 Run `python3 agents/scripts/regenerate_plan_indexes.py --check --repo-root .`.
