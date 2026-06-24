---
plan_id: 2026-06-23-17-03-35_fix-github-pages-liquid-build
title: Fix GitHub Pages Liquid Build
summary: Replace GitHub Pages-incompatible compound Liquid `where_exp` filters with page/post loops that render the same chapter, category, opportunity, and related-post lists.
status: past
created_at: 2026-06-23-17-03-35
---

# Fix GitHub Pages Liquid Build

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Identify the build failure.
  - [x] 1.1 Read the GitHub Pages error annotation supplied by the user.
  - [x] 1.2 Locate the failing `where_exp` expression in `_layouts/category.html`.
  - [x] 1.3 Search layouts, includes, and pages for other `where_exp` expressions.

- [x] 2. Replace incompatible Liquid expressions.
  - [x] 2.1 Replace category opportunity filtering with `_includes/opportunity-list.html` parameters.
  - [x] 2.2 Replace chapter opportunity filtering with `_includes/opportunity-list.html` parameters.
  - [x] 2.3 Replace `where_exp` post filtering in `_includes/related-chapter-posts.html`.
  - [x] 2.4 Replace `where_exp` post filtering in `_includes/related-opportunity-posts.html`.
  - [x] 2.5 Replace North America chapter `where_exp` filtering with a plain `where` plus loop condition.
  - [x] 2.6 Remove compound `if` expressions from updated includes.

- [x] 3. Verify the fix.
  - [x] 3.1 Confirm no `where_exp` expressions remain in layouts, includes, chapter pages, category pages, or opportunity pages.
  - [x] 3.2 Confirm no newly updated include uses compound `or ... contains` logic.
  - [-] 3.3 Run a local Jekyll build if Ruby/Jekyll tooling is available.
  - [x] 3.4 Record that local Jekyll tooling is unavailable in this environment.
