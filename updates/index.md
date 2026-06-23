---
title: Updates
description: Collaboration announcements, chapter updates, research notes, and calls for partners.
permalink: /updates/
---

{% if site.posts and site.posts.size > 0 %}
<ul class="post-list">
  {% for post in site.posts %}
  <li class="post-list-item">
    <p class="meta-row">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
      {% if post.categories and post.categories.size > 0 %} | {{ post.categories | join: ", " }}{% endif %}
    </p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.summary %}
    <p>{{ post.summary }}</p>
    {% else %}
    <p>{{ post.excerpt | strip_html | truncate: 220 }}</p>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% else %}
No updates have been published yet.
{% endif %}
