---
plan_id: 2026-06-24-08-28-15_integrate-sf-deep-research
title: Integrate SF Deep Research
summary: Integrate the completed SF Bay Area deep-research report into the BWB SF chapter opportunities, update research status, archive the report, and verify prompt generation skips integrated targets.
status: past
created_at: 2026-06-24-08-28-15
---

# Integrate SF Deep Research

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Review SF completed report.
  - [x] 1.1 Confirm report path is `research/completed/deep-research-report-sf-bay.md`.
  - [x] 1.2 Confirm chapter path is `chapters/north-america/san-francisco/index.md`.
  - [x] 1.3 Confirm the report covers all 12 category slugs.
  - [x] 1.4 Confirm no `no_good_leads_found` category needs special handling.
  - [x] 1.5 Confirm imported opportunity fields have source URLs and verification dates.
- [x] 2. Integrate SF opportunities.
  - [x] 2.1 Extract the YAML-ready opportunities from the report.
  - [x] 2.2 Remove Deep Research citation blobs from imported YAML fields.
  - [x] 2.3 Replace the SF chapter `opportunities: []` value with the selected opportunities array.
  - [x] 2.4 Preserve category slugs exactly as defined in category pages.
  - [x] 2.5 Preserve source URLs, research notes, and `last_verified` values.
- [x] 3. Update research lifecycle state.
  - [x] 3.1 Move the SF completed report to `research/archive/deep-research-report-sf-bay.md`.
  - [x] 3.2 Update every SF target in `research/status.yml` from `completed` to `integrated`.
  - [x] 3.3 Update every SF target `completed_report` path to the archive path.
  - [x] 3.4 Set every SF target `integrated_at` to `2026-06-24`.
  - [x] 3.5 Update SF target notes to state selected findings were integrated into the chapter page.
- [x] 4. Verify integration.
  - [x] 4.1 Run `python3 scripts/generate_research_prompts.py`.
  - [x] 4.2 Confirm SF generates no prompt artifact.
  - [x] 4.3 Confirm manifest counts still skip all SF targets.
  - [x] 4.4 Confirm chapter front matter has no Deep Research citation blobs.
  - [x] 4.5 Confirm SF chapter has the expected number of opportunity entries.
  - [x] 4.6 Confirm archived report is tracked and completed report path is absent.
  - [-] 4.7 Run local Jekyll validation if tooling is available.
- [x] 5. Update operational records.
  - [x] 5.1 Append a journal checkpoint.
  - [x] 5.2 Close this plan and regenerate plan indexes.
  - [x] 5.3 Review final git status and diff.
