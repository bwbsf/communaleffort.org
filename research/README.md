# Research Prompt Workflow

This directory preserves source research and tracks which chapter-category opportunity targets still need research.

## Tracked Files

- `research/status.yml` is the durable checklist for chapter-category research targets.
- `research/completed/` stores completed Deep Research or regular-prompting reports that are ready for review or integration and should be committed.
- `research/archive/` stores completed reports after their selected findings have been integrated and should be committed.
- `research/generated/` stores disposable generated prompt artifacts and is ignored by git.

Completed and archived reports are high-value source material, but they are not self-validating. Treat every report as an untrusted draft until each proposed opportunity is checked against durable public sources. Move completed reports to `research/archive/` after integration, but do not delete them; they preserve source context, caveats, and audit history.

## Generate Prompts

Use:

```bash
python3 scripts/generate_research_prompts.py
```

The generator reads chapter pages from `chapters/*/*/index.md`, collaboration categories from `categories/*/index.md`, completed-target status from `research/status.yml`, and the boilerplate at `templates/deep_research_opportunity_prompt.md`.

It writes one prompt artifact only for chapters with prompt-generating targets. Targets marked `completed`, `integrated`, or `no-good-leads` are skipped. Targets marked `needed`, `needs-rerun`, or `reset` are included in generated prompts.

## Status Values

- `needed`: research has not been completed and should generate a prompt.
- `completed`: research has been preserved in `research/completed/`, but selected opportunities have not yet been integrated.
- `integrated`: selected opportunities from the completed research have been added to the chapter page.
- `no-good-leads`: research found insufficient durable public evidence for this chapter-category target.
- `needs-rerun`: prior research should be repeated because it is stale, incomplete, or disputed.
- `reset`: imported opportunities were removed and the target should regenerate until reviewed again.

## Integrate Results

Use `playbooks/how_to_integrate_deep_research_results.md` before copying completed report findings into a chapter page. Integration must independently verify that each opportunity exists, is active or recently operational, is accurately described, has local relevance, fits the proposed category, and is an appropriate potential collaboration for the chapter. Opportunities that cannot pass validation must not be imported; the agent should explain the failed checks to the user and leave the target unintegrated or mark it for rerun. Integration should preserve `source_urls`, remove Deep Research citation blobs, localize source evidence with `scripts/localize_evidence.py`, update `research/status.yml` so completed work is not regenerated, and move the fully integrated report from `research/completed/` to `research/archive/`.

## Localize Evidence

Use `scripts/localize_evidence.py` to copy source URLs into the local `evidence/` archive before validation. The script saves ignored raw captures under `evidence/raw/`, writes committed Markdown evidence notes under `evidence/notes/`, updates `evidence/index.yml`, and writes ignored pass reports under `evidence/reports/`.

Future agents should inspect existing evidence notes before fetching sources again. Re-run localization with `--refresh` only when local evidence is missing, stale, incomplete, or disputed.

## Reset Results

If a chapter's imported opportunities are wrong or disputed, remove the affected opportunities from the chapter page, preserve the original completed or archived report, mark the affected targets `needs-rerun` or `reset` in `research/status.yml`, and rerun the generator to confirm only the intended targets return.
