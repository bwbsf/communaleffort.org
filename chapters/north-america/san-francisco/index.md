---
layout: chapter
title: San Francisco Bay Area
description: Initial chapter page for BWB SF Bay Area and its local collaboration mapping.
permalink: /chapters/north-america/san-francisco/
chapter_slug: sf-bay-area
---

{% assign chapter = site.data.chapters | where: "slug", page.chapter_slug | first %}

{% if chapter %}
## Chapter Snapshot

- **Chapter:** {{ chapter.name }}
- **Status:** {{ chapter.status }}
- **Metro / Region:** {{ chapter.city_or_area }}
- **Public site:** [{{ chapter.official_url }}]({{ chapter.official_url }})

{% if chapter.focus_areas %}
## Focus Areas

{% for area in chapter.focus_areas %}
- {{ area }}
{% endfor %}
{% endif %}

## Collaborator Inventory

This page is the chapter profile. The local collaborator list lives on the companion page:

- [San Francisco Bay Area collaborators](collaborators/)

{% else %}
Chapter data has not been added yet.
{% endif %}
