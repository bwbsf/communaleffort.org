---
plan_id: 2026-06-24-09-50-00_integrate-pending-completed-research
title: Integrate Pending Completed Research
tags: [research, governance, chapters]
status: current
created_at: 2026-06-24-09-50-00
summary: Run the completed-research integration pipeline on all currently pending completed reports with the new validation gate.
---

# Integrate Pending Completed Research

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

## Goal

Run the integration pipeline on every currently pending completed research report under `research/completed/`, importing only opportunities that pass the required validation checks and stopping on any report that is broadly unreliable or cannot be safely integrated.

## Scope

Pending completed reports at plan creation:

- `research/completed/Summary strongest UK collaboration.md`
- `research/completed/Corumbau.md`
- `research/completed/colombia.md`
- `research/completed/deep-research-report-chicago.md`
- `research/completed/deep-research-report-dc.md`
- `research/completed/deep-research-report-europe.md`
- `research/completed/deep-research-report-pdx.md`
- `research/completed/deep-research-report-sac.md`
- `research/completed/deep-research-report-vancouver-bc.md`
- `research/completed/melbourne.md`
- `research/completed/south africa.txt`

## Checklist

- [x] Inventory each pending report and match it to a chapter page.
- [x] Confirm each report has enough structured fields and source URLs for validation.
- [ ] Validate Chicago opportunities and either integrate or document failure reasons.
- [ ] Validate Washington DC opportunities and either integrate or document failure reasons.
- [ ] Validate Vancouver BC opportunities and either integrate or document failure reasons.
- [ ] Validate Portland opportunities and either integrate or document failure reasons.
- [ ] Validate Sacramento opportunities and either integrate or document failure reasons.
- [x] Validate BWB Europe opportunities and either integrate or document failure reasons.
- [ ] Validate BWB United Kingdom opportunities and either integrate or document failure reasons.
- [ ] Validate BWB South Afrika opportunities and either integrate or document failure reasons.
- [ ] Validate Corumbau opportunities and either integrate or document failure reasons.
- [ ] Validate Colombia opportunities and either integrate or document failure reasons.
- [ ] Validate Melbourne opportunities and either integrate or document failure reasons.
- [ ] Move fully integrated reports to `research/archive/` and update `research/status.yml`.
- [ ] Regenerate research prompts and confirm integrated targets are skipped.
- [ ] Add journal entries describing successful integrations and failed validation outcomes.
- [ ] Regenerate plan indexes and review git status.
