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
- `opportunities/`: Canonical collaboration opportunity pages.
- `updates/`: Public update index.
- `_posts/`: Dated updates grouped by type.
- `assets/css/`: Site styles.

## Data Files

- `_data/places.yml`: Continents and metro/region place metadata.
- `chapters/{continent}/{metro-or-region}/index.md`: Canonical chapter metadata and editable chapter notes.
- `opportunities/{continent}/{metro-or-region}/{opportunity-slug}/index.md`: Canonical opportunity metadata and editable opportunity notes.
- `categories/{category-slug}/index.md`: Canonical collaboration category metadata and category notes.

Chapter `status` values should use `active`, `dormant`, or `unknown`. Use `unknown` when a source confirms the chapter exists but does not expose a reliable per-chapter active/dormant value. Chapter directory links should point to local chapter pages; external BWB pages and social links are supporting profile links only.

Chapter contact fields include `contact_names`, `phone_numbers`, `email_addresses`, `external_websites`, and `social_media`. Copy only values visible on the matching official chapter page or another listed source, and leave empty arrays when that contact type is not published.

Opportunity pages use the same continent-to-metro/region spine as chapter pages, but they live under `opportunities/` so they remain first-class records rather than chapter-owned subpages. Link opportunities to chapters with `chapter_slugs`, to categories with `category_slug`, and to posts with `opportunity_slug` or `opportunity_slugs`.

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

Use `chapter_slug` when a post relates to one chapter and `chapter_slugs` when it relates to multiple chapters. Use `opportunity_slug` or `opportunity_slugs` when a post relates to specific opportunity pages. Use `category_slug` when a post primarily concerns one collaboration category, and `collaboration_categories` when it spans multiple categories.

Optional fields:

- `author`
- `partner_names`
- `source_urls`
- `status` for calls for partners, using values such as `open`, `filled`, or `archived`

Collaboration posts should state who collaborated, where the work happened, what community need was addressed, what each partner contributed, and what follow-up is needed. Research notes should state source status and uncertainty.

## Local Preview

If Ruby and Bundler are available, use the smallest available Jekyll build or serve command. If dependencies need network installation, ask before installing them.
