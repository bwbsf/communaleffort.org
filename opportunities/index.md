---
title: Collaboration Opportunities
description: Regional collaboration opportunity pages connected to chapters, categories, and related posts.
permalink: /opportunities/
---

Opportunity pages are first-class records. They use the same continent-to-metro/region spine as chapter pages, but they live under `opportunities/` rather than under `chapters/`.

{% assign opportunities = site.pages | where: "layout", "opportunity" | sort: "title" %}
{% include opportunity-list.html opportunities=opportunities empty_message="No opportunity pages have been added yet." %}
