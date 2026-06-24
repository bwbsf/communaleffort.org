---
title: Chapters
description: A continent-to-metro directory for Burners Without Borders chapter research.
permalink: /chapters/
---

This directory uses a **continent → metro/region** structure rather than a country-first hierarchy. The standard reflects a "Without Borders" project: country, state, and province labels are useful metadata, but they are not the public URL spine.

## Continents

{% assign chapter_pages = site.pages | where: "layout", "chapter" | sort: "metro_or_region" %}
{% assign chapter_groups = chapter_pages | group_by: "continent_name" | sort: "name" %}
{% assign chapter_group_count = chapter_groups | size %}

{% if chapter_group_count > 0 %}
<ul class="continent-list">
{% for group in chapter_groups %}
  <li><a href="#{{ group.name | slugify }}">{{ group.name }}</a></li>
{% endfor %}
</ul>
{% else %}
No chapter records have been added yet.
{% endif %}

## Chapter Records

{% if chapter_group_count > 0 %}
<div class="chapter-directory">
{% for group in chapter_groups %}
  <section class="chapter-continent-group" id="{{ group.name | slugify }}">
    <h2>{{ group.name }}</h2>
    {% assign group_chapters = group.items | sort: "metro_or_region" %}
    <div class="chapter-list">
    {% for chapter in group_chapters %}
      {% include chapter-card.html chapter=chapter %}
    {% endfor %}
    </div>
  </section>
{% endfor %}
</div>
{% endif %}
