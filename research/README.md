# Research Prompt Workflow

This directory documents the local research-prompt workflow for building chapter collaboration opportunities.

Generated prompt artifacts belong in `research/generated/`, which is intentionally ignored by git. Commit the generator script and boilerplate template, but do not commit generated prompts or manifests.

Use:

```bash
python3 scripts/generate_research_prompts.py
```

The generator reads chapter pages from `chapters/*/*/index.md`, reads collaboration categories from `categories/*/index.md`, detects missing `chapter -> category` research targets from each chapter page's `opportunities` front matter, and writes one verbose deep-research prompt artifact per chapter.
