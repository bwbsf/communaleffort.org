# Playbook: Integrate Deep Research Results

*Status: Stable*

## Objective

Safely preserve completed deep-research reports, convert selected findings into per-chapter potential collaboration opportunities, and update completion tracking so finished research is not regenerated.

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

2. **Review evidence before integration**
   * Confirm each opportunity has `organization_name`, `category_slug`, `website`, `why_it_may_fit`, `possible_collaboration_shapes`, `source_urls`, `research_notes`, and `last_verified`.
   * Confirm `source_urls` contain durable public URLs.
   * Confirm the report includes a source index or enough source context for human review.
   * Do not import opportunities that only have unsupported claims, vague geography, missing source URLs, or unclear organization status.

3. **Clean research-output formatting**
   * Remove Deep Research citation blobs such as `cite...` from imported YAML fields.
   * Keep direct public URLs in `source_urls`.
   * Keep uncertainty and caveats in `research_notes`.
   * Do not copy prose-only source claims unless they are supported by a URL in the opportunity or source index.

4. **Integrate opportunities into the chapter page**
   * Add selected entries under the chapter page's `opportunities` front matter array.
   * Keep `status: research-lead` unless the relationship has progressed.
   * Use stable kebab-case `opportunity_slug` values.
   * Preserve category slugs exactly as defined by `categories/*/index.md`.
   * Do not create standalone opportunity pages.

5. **Mark completed targets**
   * In `research/status.yml`, set a target to `integrated` when selected opportunities from that `chapter_slug` and `category_slug` have been added to the chapter page.
   * Leave a target as `completed` when the report has been preserved and reviewed but no opportunity has been imported yet.
   * Set a target to `no-good-leads` when the completed report explicitly found insufficient credible leads for that category.
   * Keep `completed_report` pointing to the preserved report path.
   * Set `integrated_at` when a target moves to `integrated`.

6. **Archive fully integrated reports**
   * After all intended findings from a completed report have been integrated or explicitly rejected, move the report from `research/completed/` to `research/archive/`.
   * Update each affected `completed_report` path in `research/status.yml` to the new archive path.
   * Keep archived reports committed; they are the audit trail for why opportunities were added, rejected, reset, or rerun.
   * Do not archive a report that still has categories awaiting review unless the status notes clearly explain the partial integration state.

7. **Regenerate prompts after integration**
   * Run `python3 scripts/generate_research_prompts.py` from the repo root.
   * Confirm completed, integrated, and no-good-leads targets do not generate boilerplate prompts.
   * Confirm generated prompt artifacts remain under ignored `research/generated/`.
   * Review `research/generated/missing-research-targets.json` for expected counts.

8. **Commit before the next report**
   * After verification passes for one completed report, commit that report's integration before starting another report.
   * Use a task-scoped commit message naming the chapter or report, such as `Integrate SF deep research opportunities`.
   * If verification fails or the report has unclear results, stop before committing or starting another report and ask for direction.
   * Do not batch multiple report integrations into one commit unless the user explicitly requests it.

9. **Reset all opportunities for a chapter if results are wrong**
   * Remove the affected entries from the chapter page's `opportunities` array.
   * In `research/status.yml`, mark every affected target `needs-rerun` or `reset`.
   * Add `notes` explaining why prior results should not be reused blindly.
   * Preserve the original completed or archived report for audit/history.
   * Regenerate prompts and confirm only the intended targets return.

10. **Reset one category for a chapter**
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
* `git status --ignored` shows generated prompt artifacts ignored and completed reports trackable.

## Plan Binding

Every integration or reset must be represented by approved active-plan checklist items before editing chapter pages, `research/status.yml`, completed reports, or generator behavior. If a report reveals new categories, stale data, or a schema gap, stop and propose plan revisions before importing results.

## Lifecycle Compliance

Prompt -> Select/Create Plan (using relevant playbook guidance) -> Request approval -> Execute approved plan atoms -> Plan update -> Docs update -> Verification.

If this occurs inside a git repo:
* Review `git status` and relevant diffs.
* Suggest a commit message that summarizes the completed checkpoint.
* Commit after each verified report integration before proceeding to another report.
