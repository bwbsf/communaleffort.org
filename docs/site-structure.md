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
- `_data/`: YAML data for places, chapters, collaborator categories, and chapter collaborators.
- `chapters/`: Public chapter and collaborator pages.
- `updates/`: Public update index.
- `_posts/`: Dated updates grouped by type.
- `assets/css/`: Site styles.

## Data Files

- `_data/collaboration_categories.yml`: Shared collaboration category definitions.
- `_data/places.yml`: Continents and metro/region place metadata.
- `_data/chapters.yml`: Chapter metadata.
- `_data/collaborators/{chapter-slug}.yml`: Potential collaborator records for one chapter.

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

Use `chapter_slug` when a post relates to a chapter. Use `collaboration_categories` when a post relates to partner categories.

Optional fields:

- `author`
- `partner_names`
- `source_urls`
- `status` for calls for partners, using values such as `open`, `filled`, or `archived`

Collaboration posts should state who collaborated, where the work happened, what community need was addressed, what each partner contributed, and what follow-up is needed. Research notes should state source status and uncertainty.

## Local Preview

If Ruby and Bundler are available, use the smallest available Jekyll build or serve command. If dependencies need network installation, ask before installing them.
