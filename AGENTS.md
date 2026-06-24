# AGENTS Instructions

Read `./agents/RULES.md` in its entirety before doing anything in this repository. Follow all instructions in `./agents/RULES.md` as though they are written directly in this file. Do not proceed if you have not read and understood `./agents/RULES.md`.

Framework resolution from the host project root:
- Use host-managed `./playbooks/`, `./references/`, `./templates/`, and `./scripts/` when present.
- Fall back to `./agents/playbooks/`, `./agents/references/`, `./agents/templates/`, and `./agents/scripts/` when host copies are missing.
- For host-owned plans, run `python3 agents/scripts/regenerate_plan_indexes.py --repo-root .`.

Host integration notes:
- This repository consumes `cjtrowbridge/agents` as a git submodule at `./agents`.
- Canonical agent policy lives in `./agents/RULES.md`.
- Runtime shim files (`AGENTS.md`, `CODEX.md`, `CLAUDE.md`, `GEMINI.md`, and `OPENCODE.md`) direct agents to that policy.
- Host-managed framework working copies live in `./playbooks/`, `./references/`, `./templates/`, and `./scripts/`.
- Host-owned operational artifacts live in `./plans/`, `./journal/`, `./kanban/`, and `./downtime/reports/`.

Website taxonomy standard:
- The public site is for Burners Without Borders chapter and collaborator mapping.
- Chapter URLs must use a continent-to-metro/region taxonomy by default: `chapters/{continent}/{metro-or-region}/`.
- Example preferred path: `chapters/north-america/san-francisco/`.
- Do not use country, state, or province as default URL hierarchy levels.
- Store country, state/province, and other formal jurisdiction labels only as metadata for search, maps, source verification, and disambiguation.
- Add a final chapter slug only when a metro/region contains multiple distinct chapters or working groups, for example `chapters/north-america/san-francisco/bwb-sf-bay-area/`.
- Disambiguate same-name places only when needed, for example `portland-oregon`, `portland-maine`, `vancouver-bc`, or `san-jose-california`.
- Prefer local identity and chapter usage over government-boundary precision when choosing public URL slugs.
- This convention is intentional: it better fits a “Without Borders” project than a jurisdiction-first hierarchy.
- Future plans, page paths, data schemas, navigation, and generated links should preserve this taxonomy unless the user explicitly approves a replacement standard.
- Chapter pages under `chapters/{continent}/{metro-or-region}/` are canonical chapter records; chapter metadata belongs in page front matter, and editable chapter notes belong in the Markdown body.
- Collaboration opportunities belong inside the relevant chapter page's `opportunities` front matter array, not in standalone opportunity pages.
- Category pages should aggregate chapter-contained opportunities by `category_slug`.
- Chapter-name links should point to local chapter pages. External websites, official BWB pages, and social links are supporting profile links only.
- The public website should use dark mode by default; new styling should use shared variables in `assets/css/site.css` instead of hard-coded light surfaces.
- Research prompt artifacts are generated local working files under `research/generated/` and must not be committed.
- The reusable research boilerplate lives at `templates/deep_research_opportunity_prompt.md`; `scripts/generate_research_prompts.py` transposes chapter and category metadata into one prompt artifact per chapter.
- Completed Deep Research and regular-prompting reports under `research/completed/` are high-value source artifacts and should be committed and preserved until integration.
- Completed reports are untrusted drafts until the integration playbook verifies each proposed opportunity's existence, active status, local relevance, category fit, source support, and appropriateness for a potential BWB collaboration.
- If an opportunity cannot be verified, do not import it into chapter front matter; explain the failed checks to the user and leave the target unintegrated or marked for rerun.
- After selected findings are integrated, move the completed report to `research/archive/` and update affected `completed_report` paths in `research/status.yml`.
- `research/status.yml` is the durable chapter-category research checklist; do not regenerate targets marked `completed`, `integrated`, or `no-good-leads` unless the user explicitly resets them.
- Use `playbooks/how_to_integrate_deep_research_results.md` before importing completed reports into chapter `opportunities` arrays or resetting prior results.
