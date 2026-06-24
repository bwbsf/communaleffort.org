# Deep Research Prompt: Collaboration Opportunities for {{ chapter_title }}

You are doing detailed civic-partnership research for Communal Effort, a project mapping Burners Without Borders chapters to practical local collaboration opportunities.

## Project Context

Communal Effort helps Burners Without Borders chapters identify existing local organizations with trust, infrastructure, expertise, resources, or public legitimacy that could strengthen chapter-led or community-led projects. The goal is not generic outreach. The goal is to produce specific, sourced, local collaboration opportunities that can be added to the chapter page as structured `opportunities` entries.

Burners Without Borders is a decentralized civic-action network connected to the Burning Man ecosystem. Relevant collaboration areas include disaster response, resilience, mutual aid, public-space stewardship, education, sustainability, arts and culture, local civic needs, and volunteer mobilization.

## Target Chapter

- Chapter title: {{ chapter_title }}
- Chapter slug: {{ chapter_slug }}
- Public site path: {{ chapter_path }}
- Continent: {{ continent_name }}
- Metro or region slug: {{ metro_or_region }}
- City or area: {{ city_or_area }}
- State or province: {{ state_or_province }}
- Country: {{ country }}
- Official BWB URL: {{ official_url }}
- Known focus areas: {{ focus_areas }}
- Existing source URLs: {{ source_urls }}

## Missing Research Targets

Research the following chapter-category targets. For each category, identify high-quality local organizations or institutions that could plausibly collaborate with this chapter.

{{ target_list }}

## What To Find For Each Opportunity

For every useful opportunity, collect enough information to create a structured entry with these fields:

```yaml
- opportunity_slug: kebab-case-local-organization-name
  organization_name: Exact public organization name
  category_slug: one-of-the-category-slugs-from-this-prompt
  status: research-lead
  website: https://example.org/
  why_it_may_fit: One concise paragraph explaining why this organization fits this BWB chapter and category.
  possible_collaboration_shapes:
    - Specific practical collaboration idea
    - Another specific practical collaboration idea
  source_urls:
    - https://source-used-for-this-claim.example/
  research_notes: Source caveats, uncertainty, contact notes, geography notes, or reasons to verify before outreach.
  last_verified: YYYY-MM-DD
```

## Research Standards

- Prefer official organization websites, official public-agency pages, reputable local directories, public filings, and credible local news.
- Include source URLs for every organization and for every important claim.
- Do not invent contact details, program details, partnerships, activity status, or geographic scope.
- Distinguish active organizations from stale, defunct, or unclear leads.
- Mark uncertainty explicitly in `research_notes`.
- Prefer organizations with local presence, public contact pathways, clear programs, and plausible ability to collaborate.
- Look for organizations that can offer venues, volunteers, materials, fiscal sponsorship, technical expertise, public legitimacy, distribution networks, training, or community relationships.
- Avoid generic national organizations unless they have a local chapter, local office, local program, or documented work in the target region.
- Do not frame recommendations around religion or faith partnerships. If a faith-affiliated organization is materially relevant because it provides nonreligious community services, describe only the practical civic-service fit neutrally.
- Do not recommend police, military, carceral, surveillance, or coercive institutions unless the category specifically requires formal public emergency coordination and the civic need cannot be described without them.
- Do not include organizations whose primary activity conflicts with inclusive civic participation or community safety.

## Category Fit Questions

For each category, answer:

1. What local organizations are credible leads for this category?
2. What specific programs, facilities, networks, or public activities make them relevant?
3. What collaboration shapes would make sense for a BWB chapter?
4. What source URLs support the recommendation?
5. What needs verification before adding or contacting the opportunity?

## Expected Final Answer

Return the results in this order:

1. A short summary of the strongest collaboration patterns for {{ city_or_area }}.
2. A YAML-ready `opportunities` list grouped by `category_slug`.
3. A `no_good_leads_found` list for any category where you could not find enough credible local evidence.
4. A `follow_up_questions` list for human review.
5. A `source_index` list of all URLs consulted with one-line notes about what each source supports.

Keep the answer detailed and evidence-oriented. The output should be usable by a maintainer who will copy selected entries into `{{ chapter_path }}` under that chapter's `opportunities` array.
