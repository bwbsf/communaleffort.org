# Playbook: Integrate Completed Research Results

*Status: Stable*

## Objective

Safely preserve completed research reports, convert only verified findings into per-chapter potential collaboration opportunities, and update completion tracking so finished research is not regenerated.

This playbook applies to both Deep Research outputs and regular-prompting research outputs. Treat every completed report as an untrusted draft until each proposed opportunity passes the validation checks below.

## Prerequisites

* Read `AGENTS.md` and `agents/RULES.md`.
* Confirm an approved active plan covers the integration checkpoint.
* Confirm the completed report exists under `research/completed/`.
* Confirm the target chapter page exists under `chapters/{continent}/{metro-or-region}/index.md`.
* Confirm `research/status.yml` exists or create it as part of the approved plan.

## Step-by-Step Instructions

1. **Select the completed report**
   * Identify the report path in `research/completed/`.
   * Identify the matching `chapter_slug` and chapter page.
   * Identify the category slugs covered by the report.
   * Preserve the completed report in git even after opportunities are integrated.
   * Keep the report in `research/completed/` while it is pending review or partial integration.

2. **Review report completeness before validation**
   * Confirm each opportunity has `organization_name`, `category_slug`, `website`, `why_it_may_fit`, `possible_collaboration_shapes`, `source_urls`, `research_notes`, and `last_verified`.
   * Confirm `source_urls` contain durable public URLs.
   * Confirm the report includes a source index or enough source context for human review.
   * Do not import opportunities that only have unsupported claims, vague geography, missing source URLs, or unclear organization status.

3. **Validate each opportunity before integration**
   * Verify the organization exists using an official website, official public-agency page, reputable directory, public filing, or credible local source.
   * Verify the organization appears active or recently operational; do not import stale, defunct, dormant, or unclear leads without explicit user approval.
   * Verify the organization has real local relevance to the target chapter's metro/region, such as a local office, local program, local service area, local events, or documented local work.
   * Verify the proposed category is accurate by matching the organization's public programs, facilities, services, or mission to the category page definition.
   * Verify each major claim in `why_it_may_fit`, `possible_collaboration_shapes`, and `research_notes` is supported by at least one `source_urls` entry.
   * Verify the opportunity has a plausible non-extractive collaboration path for a BWB chapter, such as volunteer coordination, venue access, materials, training, fiscal sponsorship, public legitimacy, distribution networks, technical expertise, or community relationships.
   * Verify the proposed collaboration does not depend on religious outreach, partisan alignment, coercive institutions, surveillance, carceral systems, or organizations whose primary activity conflicts with inclusive civic participation or community safety.
   * Verify public contact or engagement pathways where possible, such as a contact page, email, phone number, volunteer form, program page, or social profile. Record missing contact pathways in `research_notes`.
   * Set or refresh `last_verified` to the date the agent performed these checks.
   * Do not rely on the report's prose alone; independently open or inspect enough sources to confirm existence, description, local relevance, and fit.

4. **Fail closed when validation is incomplete**
   * If any required validation check cannot be completed, do not import that opportunity.
   * Leave the affected target as `completed`, `needs-rerun`, or `reset` rather than `integrated`, depending on whether more work or a fresh prompt is needed.
   * Explain the failed checks to the user with the organization name, category slug, missing or conflicting evidence, and what would be needed to reconsider it.
   * If all opportunities in a category fail validation, do not mark the category `integrated`; use `no-good-leads` only when the report credibly supports that conclusion.
   * If validation reveals a report is broadly unreliable, stop the integration checkpoint before editing chapter opportunities and ask the user whether to rerun or discard that report.

5. **Clean research-output formatting**
   * Remove Deep Research citation blobs such as `cite...` from imported YAML fields.
   * Keep direct public URLs in `source_urls`.
   * Keep uncertainty and caveats in `research_notes`.
   * Do not copy prose-only source claims unless they are supported by a URL in the opportunity or source index.

6. **Integrate validated opportunities into the chapter page**
   * Add selected entries under the chapter page's `opportunities` front matter array.
   * Keep `status: research-lead` unless the relationship has progressed.
   * Use stable kebab-case `opportunity_slug` values.
   * Preserve category slugs exactly as defined by `categories/*/index.md`.
   * Do not create standalone opportunity pages.
   * Import only opportunities that passed the validation gate.
   * Keep validation caveats in `research_notes` rather than overstating certainty.

7. **Mark completed targets**
   * In `research/status.yml`, set a target to `integrated` when selected opportunities from that `chapter_slug` and `category_slug` have been added to the chapter page.
   * Leave a target as `completed` when the report has been preserved and reviewed but no opportunity has been imported yet.
   * Set a target to `no-good-leads` when the completed report explicitly found insufficient credible leads for that category.
   * Keep `completed_report` pointing to the preserved report path.
   * Set `integrated_at` when a target moves to `integrated`.

8. **Archive fully integrated reports**
   * After all intended findings from a completed report have been integrated or explicitly rejected, move the report from `research/completed/` to `research/archive/`.
   * Update each affected `completed_report` path in `research/status.yml` to the new archive path.
   * Keep archived reports committed; they are the audit trail for why opportunities were added, rejected, reset, or rerun.
   * Do not archive a report that still has categories awaiting review unless the status notes clearly explain the partial integration state.

9. **Regenerate prompts after integration**
   * Run `python3 scripts/generate_research_prompts.py` from the repo root.
   * Confirm completed, integrated, and no-good-leads targets do not generate boilerplate prompts.
   * Confirm generated prompt artifacts remain under ignored `research/generated/`.
   * Review `research/generated/missing-research-targets.json` for expected counts.

10. **Commit before the next report**
   * After verification passes for one completed report, commit that report's integration before starting another report.
   * Use a task-scoped commit message naming the chapter or report, such as `Integrate SF deep research opportunities`.
   * If verification fails or the report has unclear results, stop before committing or starting another report and ask for direction.
   * Do not batch multiple report integrations into one commit unless the user explicitly requests it.

11. **Reset all opportunities for a chapter if results are wrong**
   * Remove the affected entries from the chapter page's `opportunities` array.
   * In `research/status.yml`, mark every affected target `needs-rerun` or `reset`.
   * Add `notes` explaining why prior results should not be reused blindly.
   * Preserve the original completed or archived report for audit/history.
   * Regenerate prompts and confirm only the intended targets return.

12. **Reset one category for a chapter**
   * Remove only opportunities matching that `category_slug` from the chapter page.
   * Mark only that `chapter_slug` + `category_slug` target as `needs-rerun` or `reset`.
   * Keep unrelated category targets unchanged.
   * Regenerate prompts and confirm the regenerated artifact contains that category and not completed categories.

## Verification

* `research/completed/` or `research/archive/` report remains tracked or staged for commit.
* `research/status.yml` reflects each target state accurately.
* `python3 scripts/generate_research_prompts.py` completes successfully.
* `research/generated/missing-research-targets.json` shows completed/integrated/no-good-leads targets as skipped.
* Chapter page YAML contains no Deep Research citation blobs.
* Chapter page opportunity entries include source URLs and verification dates.
* Every imported opportunity has evidence for organization existence, active status, local relevance, category fit, collaboration appropriateness, and contact or engagement pathways where available.
* Any opportunity that failed validation was excluded, and the user-facing checkpoint summary explains why it was not integrated.
* `git status --ignored` shows generated prompt artifacts ignored and completed reports trackable.

## Plan Binding

Every integration or reset must be represented by approved active-plan checklist items before editing chapter pages, `research/status.yml`, completed reports, or generator behavior. If a report reveals new categories, stale data, or a schema gap, stop and propose plan revisions before importing results.

## Lifecycle Compliance

Prompt -> Select/Create Plan (using relevant playbook guidance) -> Request approval -> Execute approved plan atoms -> Plan update -> Docs update -> Verification.

If this occurs inside a git repo:
* Review `git status` and relevant diffs.
* Suggest a commit message that summarizes the completed checkpoint.
* Commit after each verified report integration before proceeding to another report.
