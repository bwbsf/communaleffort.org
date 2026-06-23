---
title: Chapters
description: A continent-to-metro directory for Burners Without Borders chapter research.
permalink: /chapters/
---

This directory uses a **continent → metro/region** structure rather than a country-first hierarchy. The standard reflects a "Without Borders" project: country, state, and province labels are useful metadata, but they are not the public URL spine.

## Continents

- [North America](north-america/)

## Initial Chapter Records

{% assign chapters = site.data.chapters %}
{% if chapters and chapters.size > 0 %}
<div class="grid-cards">
{% for chapter in chapters %}
  {% include chapter-card.html chapter=chapter %}
{% endfor %}
</div>
{% else %}
No chapter records have been added yet.
{% endif %}
