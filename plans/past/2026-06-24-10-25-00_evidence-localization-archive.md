---
plan_id: 2026-06-24-10-25-00_evidence-localization-archive
title: Evidence Localization Archive
tags: [research, evidence, governance]
status: past
created_at: 2026-06-24-10-25-00
summary: Add an evidence archive workflow that localizes source URLs once, records reusable citation metadata, and lets future validation use local evidence notes before re-fetching websites.
---

# Evidence Localization Archive

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

## Goal

Create a reusable `./evidence` system for localizing research source URLs into ignored raw captures plus committed Markdown evidence notes and a manifest. The workflow should skip already-localized URLs, report where local evidence lives, and update playbooks/agent instructions so future integration passes use local evidence before fetching remote pages again.

## Checklist

- [x] Create `evidence/` with committed governance documentation and keep-file placeholders.
- [x] Add ignore rules for raw localized captures and generated localization reports.
- [x] Add a script that accepts source URLs from chapter files, research reports, or explicit URL arguments.
- [x] Make the script skip URLs already present in the evidence manifest unless refresh is requested.
- [x] Make the script save raw captures locally, create Markdown evidence notes, and update a committed manifest.
- [x] Make the script produce a machine-readable and human-readable pass report showing localized, skipped, and failed URLs plus evidence paths.
- [x] Update the research integration playbook to require evidence localization before importing opportunities when sources are available.
- [x] Update `AGENTS.md` so future agents know the evidence archive standard.
- [x] Update supporting research/site docs to explain the workflow.
- [x] Add a journal entry for the evidence archive implementation.
- [x] Regenerate plan indexes.
- [x] Verify script help, dry-run/empty behavior, and syntax without requiring network access.
