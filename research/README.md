# Research Prompt Workflow

This directory preserves source research and tracks which chapter-category opportunity targets still need deep research.

## Tracked Files

- `research/status.yml` is the durable checklist for chapter-category research targets.
- `research/completed/` stores completed deep-research reports that are ready for review or integration and should be committed.
- `research/archive/` stores completed reports after their selected findings have been integrated and should be committed.
- `research/generated/` stores disposable generated prompt artifacts and is ignored by git.

Completed and archived reports are high-value source material. Move completed reports to `research/archive/` after integration, but do not delete them; they preserve source context, caveats, and audit history.

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

Use `playbooks/how_to_integrate_deep_research_results.md` before copying completed report findings into a chapter page. Integration should preserve `source_urls`, remove Deep Research citation blobs, update `research/status.yml` so completed work is not regenerated, and move the fully integrated report from `research/completed/` to `research/archive/`.

## Reset Results

If a chapter's imported opportunities are wrong or disputed, remove the affected opportunities from the chapter page, preserve the original completed or archived report, mark the affected targets `needs-rerun` or `reset` in `research/status.yml`, and rerun the generator to confirm only the intended targets return.
