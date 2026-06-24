---
plan_id: 2026-06-23-17-27-13_research-prompt-generator
title: Research Prompt Generator
summary: Create an ignored generated-artifact workflow for chapter-by-category collaboration research prompts.
status: past
created_at: 2026-06-23-17-27-13
---

# Research Prompt Generator

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Confirm source content model.
  - [x] 1.1 Read representative chapter front matter.
  - [x] 1.2 Read representative category front matter.
  - [x] 1.3 Confirm generated prompt artifacts should not be committed.
- [x] 2. Add ignored research artifact directory.
  - [x] 2.1 Add ignore rules for generated research prompt artifacts.
  - [x] 2.2 Add tracked documentation for the research workflow directory.
  - [x] 2.3 Ensure generated prompts and manifests are excluded from commits.
- [x] 3. Add reusable prompt boilerplate.
  - [x] 3.1 Create a boilerplate template for deep research tasks.
  - [x] 3.2 Include project context, chapter context, categories, evidence rules, exclusions, and output schema.
  - [x] 3.3 Include YAML-ready opportunity field requirements matching chapter `opportunities` arrays.
- [x] 4. Add prompt generation script.
  - [x] 4.1 Read chapter pages from `chapters/*/*/index.md`.
  - [x] 4.2 Read category pages from `categories/*/index.md`.
  - [x] 4.3 Detect missing chapter-category research targets based on absent nested opportunities.
  - [x] 4.4 Generate one verbose prompt artifact per chapter.
  - [x] 4.5 Generate a machine-readable missing-target manifest.
  - [x] 4.6 Keep generation deterministic and local-only.
- [x] 5. Document and log the workflow.
  - [x] 5.1 Update site structure documentation with the research prompt workflow.
  - [x] 5.2 Add a journal checkpoint describing the implementation.
  - [x] 5.3 Regenerate plan indexes after plan updates.
- [x] 6. Verify implementation.
  - [x] 6.1 Run the generator script.
  - [x] 6.2 Confirm one prompt artifact is produced per chapter.
  - [x] 6.3 Confirm missing targets equal chapter count times categories minus existing opportunity coverage.
  - [x] 6.4 Confirm generated artifacts are ignored by git.
  - [x] 6.5 Review final repository status and diff.
