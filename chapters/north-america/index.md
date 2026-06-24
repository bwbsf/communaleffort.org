---
title: North America
description: Metro/region pages for North American Burners Without Borders chapter research.
permalink: /chapters/north-america/
---

North American chapter pages are organized by commonly recognized metro or regional identity.

## Metro / Region Pages

{% assign north_america_chapters = site.pages | where: "layout", "chapter" | sort: "metro_or_region" %}

{% assign rendered_chapter_count = 0 %}
<ul class="chapter-list">
{% for chapter in north_america_chapters %}
  {% if chapter.continent == 'north-america' %}
  {% assign rendered_chapter_count = rendered_chapter_count | plus: 1 %}
  {% include chapter-card.html chapter=chapter %}
  {% endif %}
{% endfor %}
</ul>
{% if rendered_chapter_count == 0 %}
No North American chapter pages have been added yet.
{% endif %}
