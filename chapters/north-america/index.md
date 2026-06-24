---
title: North America
description: Metro/region pages for North American Burners Without Borders chapter research.
permalink: /chapters/north-america/
---

North American chapter pages are organized by commonly recognized metro or regional identity.

## Metro / Region Pages

{% assign north_america_chapters = site.pages | where_exp: "chapter", "chapter.layout == 'chapter' and chapter.continent == 'north-america'" | sort: "metro_or_region" %}

{% if north_america_chapters and north_america_chapters.size > 0 %}
<ul class="chapter-list">
{% for chapter in north_america_chapters %}
  {% include chapter-card.html chapter=chapter %}
{% endfor %}
</ul>
{% else %}
No North American chapter pages have been added yet.
{% endif %}
