---
plan_id: 2026-06-24-08-47-40_category-generated-opportunity-lists
title: Category Generated Opportunity Lists
summary: Clarify category pages by adding a generated opportunity-list explanation and rendering all matching chapter opportunities as category examples.
status: past
created_at: 2026-06-24-08-47-40
---

# Category Generated Opportunity Lists

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Review category rendering.
  - [x] 1.1 Confirm category pages use `_layouts/category.html`.
  - [x] 1.2 Confirm opportunities are sourced from chapter page front matter.
- [x] 2. Update category page content.
  - [x] 2.1 Add a brief explanation above the generated category opportunity list.
  - [x] 2.2 Show that the list is generated from chapter `opportunities` entries matching `category_slug`.
  - [x] 2.3 Keep category front matter `examples` visible as typical collaboration shapes.
  - [x] 2.4 Keep every listed item linked to its source chapter and external organization website when available.
- [x] 3. Update documentation and logs.
  - [x] 3.1 Update site-structure docs if category aggregation behavior changes materially.
  - [x] 3.2 Append a journal checkpoint.
  - [x] 3.3 Archive this plan and regenerate indexes.
- [x] 4. Verify category rendering.
  - [x] 4.1 Run static checks for risky Liquid syntax.
  - [x] 4.2 Confirm category pages still aggregate matching opportunities.
  - [-] 4.3 Run local Jekyll validation if tooling is available.
  - [x] 4.4 Review git status and diff.
