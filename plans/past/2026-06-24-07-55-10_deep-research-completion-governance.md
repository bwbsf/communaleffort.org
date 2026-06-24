---
plan_id: 2026-06-24-07-55-10_deep-research-completion-governance
title: Deep Research Completion Governance
summary: Preserve completed deep-research reports, track completed chapter-category targets, skip completed targets in prompt generation, add integration/reset playbook governance, and update chapter opportunity/volunteer presentation.
status: past
created_at: 2026-06-24-07-55-10
---

# Deep Research Completion Governance

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Confirm completed research quality and scope.
  - [x] 1.1 Read every file in `research/completed/`.
  - [x] 1.2 Count opportunity entries in each completed report.
  - [x] 1.3 Count category coverage in each completed report.
  - [x] 1.4 Identify categories reported as `no_good_leads_found`.
  - [x] 1.5 Identify formatting hazards such as Deep Research citation blobs.
  - [x] 1.6 Record which completed reports are ready for preservation.
  - [x] 1.7 Record which completed reports need cleanup before integration.

- [x] 2. Define durable completed-research metadata.
  - [x] 2.1 Choose the canonical tracking file path, expected to be `research/status.yml`.
  - [x] 2.2 Define one record per `chapter_slug` and `category_slug` target.
  - [x] 2.3 Define allowed target statuses: `needed`, `completed`, `integrated`, `no-good-leads`, `needs-rerun`, and `reset`.
  - [x] 2.4 Define required target fields: `chapter_slug`, `category_slug`, `status`, `completed_report`, `completed_at`, `integrated_at`, `notes`.
  - [x] 2.5 Define how completed whole-chapter reports map to all categories found in that report.
  - [x] 2.6 Define how `no_good_leads_found` categories are represented without forcing reruns.
  - [x] 2.7 Define how stale or disputed research is marked for rerun.

- [x] 3. Preserve completed deep-research reports.
  - [x] 3.1 Confirm `research/completed/` is tracked and not ignored.
  - [x] 3.2 Decide whether report filenames need date prefixes or whether status metadata is sufficient.
  - [-] 3.3 Add front matter to completed reports if needed for chapter/date/status metadata.
  - [x] 3.4 Ensure completed reports keep full source context and source indexes.
  - [x] 3.5 Ensure completed reports are committed as high-value content.
  - [x] 3.6 Document that completed reports must not be deleted merely because opportunities are integrated.

- [x] 4. Update prompt generation to skip completed work.
  - [x] 4.1 Read `research/status.yml` when present.
  - [x] 4.2 Treat `completed`, `integrated`, and `no-good-leads` targets as not missing.
  - [x] 4.3 Treat `needed`, `needs-rerun`, and `reset` targets as prompt-generating targets.
  - [x] 4.4 Keep existing chapter-front-matter opportunity coverage as an additional skip signal.
  - [x] 4.5 Generate no prompt artifact when a chapter has zero prompt-generating targets.
  - [x] 4.6 Update `missing-research-targets.json` so it reports skipped/completed/integrated/no-good-leads counts.
  - [x] 4.7 Include status-file provenance in the generated manifest.
  - [x] 4.8 Preserve deterministic output paths and ordering.

- [x] 5. Update research prompt boilerplate.
  - [x] 5.1 Instruct Deep Research outputs to omit proprietary citation blobs from YAML fields.
  - [x] 5.2 Require direct `source_urls` for every opportunity.
  - [x] 5.3 Require `source_index` with URL notes.
  - [x] 5.4 Require `no_good_leads_found` entries for categories without enough evidence.
  - [x] 5.5 Ask the research tool to avoid repeating already completed categories when the prompt includes a partial target list.

- [x] 6. Create integration playbook.
  - [x] 6.1 Add `playbooks/how_to_integrate_deep_research_results.md`.
  - [x] 6.2 Explain how to select one completed report and matching chapter page.
  - [x] 6.3 Explain how to review evidence quality before integration.
  - [x] 6.4 Explain how to strip Deep Research citation blobs before copying opportunities.
  - [x] 6.5 Explain how to copy selected opportunities into the chapter page `opportunities` array.
  - [x] 6.6 Explain how to preserve `source_urls`, `research_notes`, and `last_verified`.
  - [x] 6.7 Explain how to mark targets `integrated` in `research/status.yml`.
  - [x] 6.8 Explain how to leave targets `completed` when reviewed but not yet integrated.
  - [x] 6.9 Explain how to mark `no-good-leads` categories.
  - [x] 6.10 Explain how to regenerate prompts after integration.
  - [x] 6.11 Explain how to verify completed/integrated targets are not regenerated.
  - [x] 6.12 Explain commit boundaries for preserving reports and integrating chapter opportunities.

- [x] 7. Document reset and removal workflow.
  - [x] 7.1 Define how to remove all opportunities for a chapter when research is wrong or disputed.
  - [x] 7.2 Define how to remove only one category's opportunities from a chapter.
  - [x] 7.3 Define how to mark affected status records as `needs-rerun` or `reset`.
  - [x] 7.4 Define how to preserve the original completed report even when opportunities are removed.
  - [x] 7.5 Define how to add reset notes explaining why the prior results should not be reused blindly.
  - [x] 7.6 Define verification steps after reset so prompts regenerate only the intended targets.

- [x] 8. Update public chapter presentation.
  - [x] 8.1 Change the per-chapter heading from `Collaboration Opportunities` to `Potential Collaboration Opportunities`.
  - [x] 8.2 Add a `Volunteer With This Chapter` section above potential opportunities.
  - [x] 8.3 Define chapter front matter fields for volunteer guidance, such as `volunteer_summary` and `volunteer_links`.
  - [x] 8.4 Render chapter-specific volunteer fields when present.
  - [x] 8.5 Render a useful fallback using official chapter, external website, social, or email links when volunteer fields are absent.
  - [x] 8.6 Ensure the volunteer section does not duplicate the existing contact/profile section too heavily.
  - [x] 8.7 Keep language human-oriented and action-focused.

- [x] 9. Update documentation and indexes.
  - [x] 9.1 Update `research/README.md` with completed-report, status-file, generation, integration, and reset rules.
  - [x] 9.2 Update `docs/site-structure.md` with the completed-research tracking model.
  - [x] 9.3 Update `AGENTS.md` with durable standards for preserving completed research and not regenerating completed targets.
  - [-] 9.4 Update `RULES.md` playbook index after adding the integration playbook.
  - [-] 9.5 Update `README.md` only if the public project overview needs to mention the volunteer or research workflow changes.
  - [x] 9.6 Append a journal checkpoint for implementation work.
  - [x] 9.7 Regenerate plan indexes after plan lifecycle changes.

- [x] 10. Verify the full workflow.
  - [x] 10.1 Run `python3 scripts/generate_research_prompts.py`.
  - [x] 10.2 Confirm completed targets from `research/status.yml` do not generate boilerplate prompts.
  - [x] 10.3 Confirm reset or needs-rerun targets do generate prompts.
  - [x] 10.4 Confirm generated prompt artifacts remain ignored by git.
  - [x] 10.5 Confirm completed research reports and status YAML are tracked by git.
  - [x] 10.6 Confirm chapter pages render the new volunteer heading and `Potential Collaboration Opportunities` heading.
  - [x] 10.7 Run static checks for citation blobs in chapter opportunity YAML after any integration.
  - [-] 10.8 Run local Jekyll validation if Ruby/Jekyll tooling is available.
  - [x] 10.9 If local Jekyll tooling is unavailable, note that GitHub Pages must validate the build.
  - [x] 10.10 Review `git status` and relevant diffs before commit.
