---
title: Chapters
description: A continent-to-metro directory for Burners Without Borders chapter research.
permalink: /chapters/
---

This directory uses a **continent → metro/region** structure rather than a country-first hierarchy. The standard reflects a "Without Borders" project: country, state, and province labels are useful metadata, but they are not the public URL spine.

## Continents

{% assign chapter_pages = site.pages | where: "layout", "chapter" | sort: "metro_or_region" %}
{% assign chapter_groups = chapter_pages | group_by: "continent_name" | sort: "name" %}

{% if chapter_groups and chapter_groups.size > 0 %}
<ul class="inline-list">
{% for group in chapter_groups %}
  <li><a href="#{{ group.name | slugify }}">{{ group.name }}</a></li>
{% endfor %}
</ul>
{% else %}
No chapter records have been added yet.
{% endif %}

## Chapter Records

{% if chapter_groups and chapter_groups.size > 0 %}
<div class="chapter-directory">
{% for group in chapter_groups %}
  <section class="chapter-continent-group" id="{{ group.name | slugify }}">
    <h2>{{ group.name }}</h2>
    {% assign group_chapters = group.items | sort: "metro_or_region" %}
    <ul class="chapter-list">
    {% for chapter in group_chapters %}
      {% include chapter-card.html chapter=chapter %}
    {% endfor %}
    </ul>
  </section>
{% endfor %}
</div>
{% endif %}
