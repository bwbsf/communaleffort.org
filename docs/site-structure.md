# Site Structure

This project uses GitHub Pages and Jekyll.

## Homepage

- `README.md` remains the homepage source and normal GitHub README.
- Do not add YAML front matter to `README.md`.
- `_config.yml` assigns the `readme-home` layout and `/` permalink through front matter defaults.
- Do not create root `index.md` or `index.html` unless validation proves it is necessary and the user approves the fallback.
- GitHub Pages enables `jekyll-optional-front-matter` and `jekyll-readme-index` by default, so the clean README strategy depends on the GitHub Pages build environment.

## Chapter URLs

Chapter pages use a continent-to-metro/region taxonomy:

```text
chapters/{continent}/{metro-or-region}/
```

Example:

```text
chapters/north-america/san-francisco/
```

Country, state, and province labels are metadata only. They should not become default URL path levels.

## Core Directories

- `_layouts/`: Shared page, post, chapter, and README-home wrappers.
- `_includes/`: Reusable navigation, cards, lists, and post summaries.
- `_data/`: Shared support data when a content type does not need its own page collection.
- `chapters/`: Canonical chapter profile pages.
- `updates/`: Public update index.
- `_posts/`: Dated updates grouped by type.
- `assets/css/`: Site styles.
- `research/`: Tracked research workflow notes; generated prompt artifacts are written under ignored `research/generated/`.
- `templates/`: Reusable project templates, including the deep-research opportunity prompt boilerplate.
- `scripts/`: Local automation, including prompt generation.

## Data Files

- `_data/places.yml`: Continents and metro/region place metadata.
- `chapters/{continent}/{metro-or-region}/index.md`: Canonical chapter metadata and editable chapter notes.
- `categories/{category-slug}/index.md`: Canonical collaboration category metadata and category notes.

Chapter `status` values should use `active`, `dormant`, or `unknown`. Use `unknown` when a source confirms the chapter exists but does not expose a reliable per-chapter active/dormant value. Chapter directory links should point to local chapter pages; external BWB pages and social links are supporting profile links only.

Chapter contact fields include `contact_names`, `phone_numbers`, `email_addresses`, `external_websites`, and `social_media`. Copy only values visible on the matching official chapter page or another listed source, and leave empty arrays when that contact type is not published.

Chapter collaboration opportunities live inside each chapter page's front matter as an `opportunities` array. Each opportunity can include `opportunity_slug`, `organization_name`, `category_slug`, `status`, `website`, `why_it_may_fit`, `possible_collaboration_shapes`, `source_urls`, `research_notes`, and `last_verified`.

Category pages aggregate opportunities from chapter front matter by matching `category_slug`. Do not create standalone opportunity pages unless the user explicitly changes this content model.

Chapter volunteer guidance can use optional `volunteer_summary` text and `volunteer_links` entries with `label` and `url`. When those fields are absent, chapter pages render fallback volunteer links from official chapter, external website, social, or email contact fields.

## Research Prompt Workflow

Use `scripts/generate_research_prompts.py` to create deep-research prompt artifacts for missing chapter-category opportunity targets. The script reads chapter pages, category pages, `research/status.yml`, and `templates/deep_research_opportunity_prompt.md`, then writes one verbose prompt per chapter with remaining prompt-generating targets plus a missing-target manifest under `research/generated/`.

`research/status.yml` is the durable chapter-category checklist. Targets marked `completed`, `integrated`, or `no-good-leads` are skipped by the generator; targets marked `needed`, `needs-rerun`, or `reset` are regenerated.

`research/completed/` stores completed deep-research reports awaiting review or integration. `research/archive/` stores completed reports after their selected findings have been integrated. Both completed and archived reports should be committed as high-value source material. `research/generated/` is intentionally ignored by git; do not commit generated prompts or manifests.

## Post Types

Use subdirectories under `_posts/`:

- `_posts/collaborations/`
- `_posts/chapter-updates/`
- `_posts/research-notes/`
- `_posts/calls-for-partners/`

Do not add sample posts unless the user approves them.

## Post Front Matter

Required fields:

- `title`
- `date`
- `categories`
- `summary`

Use `chapter_slug` when a post relates to one chapter and `chapter_slugs` when it relates to multiple chapters. Use `opportunity_slug` or `opportunity_slugs` when a post relates to specific chapter-contained opportunities. Use `category_slug` when a post primarily concerns one collaboration category, and `collaboration_categories` when it spans multiple categories.

Optional fields:

- `author`
- `partner_names`
- `source_urls`
- `status` for calls for partners, using values such as `open`, `filled`, or `archived`

Collaboration posts should state who collaborated, where the work happened, what community need was addressed, what each partner contributed, and what follow-up is needed. Research notes should state source status and uncertainty.

## Visual Standard

The public site uses dark mode by default. New layouts, includes, and content components should use the shared CSS variables in `assets/css/site.css` rather than hard-coded light surfaces.

## Local Preview

If Ruby and Bundler are available, use the smallest available Jekyll build or serve command. If dependencies need network installation, ask before installing them.
