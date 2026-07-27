---
plan_id: 2026-07-27-13-28-57_repair-chapter-yaml-front-matter
title: Repair Chapter YAML Front Matter
summary: Restore valid YAML front matter for all chapter pages currently blocking reliable Jekyll rendering.
status: current
created_at: 2026-07-27-13-28-57
---

# Repair Chapter YAML Front Matter

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

- [x] 1. Restore parseable chapter metadata without changing the intended chapter or opportunity content.
  - [x] 1.1 Repair unquoted colon-containing scalar values.
    - [x] 1.1.1 Quote affected organization names and prose values in Detroit, Galveston, Heartland, Houston, Madison, Orange County, Reno, and Utah.
  - [x] 1.2 Repair malformed opportunity-list structure.
    - [x] 1.2.1 Correct misplaced or over-indented YAML nodes in United Kingdom, Chicago, Sacramento, Washington D.C., Melbourne, Perth, Sydney, Colombia, and Corumbau.
  - [x] 1.3 Remove non-YAML markup from chapter metadata.
    - [x] 1.3.1 Remove the stray code fence from Vancouver's front matter.
  - [x] 1.4 Recover valid chapter data from pasted research-report artifacts.
    - [x] 1.4.1 Record the pre-recovery opportunity slugs and counts for each recovery target: United Kingdom 25, Chicago 17, Sacramento 24, Washington D.C. 35, Melbourne 31, Perth 25, Sydney 23, and Colombia 21.
    - [x] 1.4.2 Remove report-only Markdown, citation definitions, source indexes, and follow-up question blocks embedded in those files' YAML front matter.
    - [x] 1.4.3 Restore every preserved opportunity record to the chapter's `opportunities` array before its `sources` field and closing front-matter delimiter.
    - [x] 1.4.4 Compare post-recovery opportunity slugs and counts with the recorded baseline; every recovered file retained its baseline count.
    - [x] 1.4.5 Confirm every recovered file has exactly one closing front-matter delimiter, a YAML `sources` list, and Markdown body content only after that delimiter.
    - [x] 1.4.6 Treat every proposed deletion as report-only unless it is a structured chapter field or an `opportunity_slug` record; no uncertain classification remained.

- [?] 2. Verify the repair and preserve the project workflow record.
  - [x] 2.1 Parse every canonical chapter front matter block with a YAML parser; all 46 chapter files pass.
  - [?] 2.2 Run the available Jekyll-compatible site build or validation command without installing dependencies; no local `Gemfile`, `bundle`, or `jekyll` executable is available.
  - [x] 2.3 Review the changed files and update this plan and its status index to match the verified result.
  - [?] 2.4 Treat a successful YAML parse and Jekyll-compatible build as the acceptance criteria; the YAML criterion passes, while build validation remains unavailable locally.
