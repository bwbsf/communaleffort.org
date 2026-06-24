---
plan_id: 2026-06-24-09-50-00_integrate-pending-completed-research
title: Integrate Pending Completed Research
tags: [research, governance, chapters]
status: current
created_at: 2026-06-24-09-50-00
summary: Run the completed-research integration pipeline on all currently pending completed reports with the new validation gate.
---

# Integrate Pending Completed Research

Key: `[ ]` pending task, `[x]` completed task, `[?]` needs validation, `[-]` closed task

## Goal

Run the integration pipeline on every currently pending completed research report under `research/completed/`, importing only opportunities that pass the required validation checks and stopping on any report that is broadly unreliable or cannot be safely integrated.

## Scope

Pending completed reports at plan creation:

- `research/completed/Summary strongest UK collaboration.md`
- `research/completed/Corumbau.md`
- `research/completed/colombia.md`
- `research/completed/deep-research-report-chicago.md`
- `research/completed/deep-research-report-dc.md`
- `research/completed/deep-research-report-europe.md`
- `research/completed/deep-research-report-pdx.md`
- `research/completed/deep-research-report-sac.md`
- `research/completed/deep-research-report-vancouver-bc.md`
- `research/completed/melbourne.md`
- `research/completed/perth.md`
- `research/completed/south africa.txt`
- `research/completed/sydney.md`

## Checklist

- [x] Inventory each pending report and match it to a chapter page.
- [x] Confirm each report has enough structured fields and source URLs for validation.
- [x] Validate Chicago opportunities and either integrate or document failure reasons.
- [x] Validate Washington DC opportunities and either integrate or document failure reasons.
- [x] Validate Vancouver BC opportunities and either integrate or document failure reasons.
- [x] Validate Portland opportunities and either integrate or document failure reasons.
- [x] Validate Sacramento opportunities and either integrate or document failure reasons.
- [x] Validate BWB Europe opportunities and either integrate or document failure reasons.
- [x] Validate BWB United Kingdom opportunities and either integrate or document failure reasons.
- [?] Validate BWB South Afrika opportunities and either integrate or document failure reasons.
- [x] Validate Corumbau opportunities and either integrate or document failure reasons.
- [x] Validate Colombia opportunities and either integrate or document failure reasons.
- [x] Validate Melbourne opportunities and either integrate or document failure reasons.
- [x] Validate Perth opportunities and either integrate or document failure reasons.
- [x] Validate Sydney opportunities and either integrate or document failure reasons.
- [x] Move fully integrated reports to `research/archive/` and update `research/status.yml`.
- [x] Regenerate research prompts and confirm integrated targets are skipped.
- [ ] Add journal entries describing successful integrations and failed validation outcomes.
- [ ] Regenerate plan indexes and review git status.

## Validation Outcomes

- BWB United Kingdom: integrated; imported 25; excluded 2; excluded leads: Unite Community (labor-unions-worker-centers), London Resilience Partnership (local-government-public-agencies).
- Corumbau: integrated; imported 18; excluded 5; excluded leads: Colônia de Pescadores Z-23 de Prado (labor-unions-worker-centers), Federação das Associações da Reserva Extrativista Marinha do Corumbau – FAREMCO (mutual-aid-groups), Associação da Reserva Extrativista Marinha de Corumbau – AREMACO (nonprofits-cbos), Associação dos Pescadores de Cumuruxatiba – APEC (nonprofits-cbos), Escola Municipal de Corumbau (schools-libraries-community-centers).
- Colombia: integrated; imported 18; excluded 3; excluded leads: Escuela Nacional Sindical (labor-unions-worker-centers), Unidad Nacional para la Gestión del Riesgo de Desastres (local-government-public-agencies), Instituto Distrital de Gestión de Riesgos y Cambio Climático - IDIGER (local-government-public-agencies).
- Chicago: integrated; imported 17; excluded 3; excluded leads: Openlands (environmental-resilience-organizations), The Chicago Community Trust (funders-fiscal-sponsors), Edgewater Mutual Aid Network (EMAN) (mutual-aid-groups).
- Washington DC: integrated; imported 27; excluded 1; excluded leads: Food Not Bombs Washington, DC (mutual-aid-groups).
- Sacramento: integrated; imported 24; excluded 3; excluded leads: Sacramento Tree Foundation (environmental-resilience-organizations), Sacramento Region Community Foundation (funders-fiscal-sponsors), United Way California Capital Region (nonprofits-cbos).
- Vancouver BC: integrated; imported 26; excluded 7; excluded leads: Lookout Housing and Health Society (direct-service-providers), City of Vancouver (local-government-public-agencies), City of Vancouver (local-government-public-agencies), City of Vancouver (local-government-public-agencies), Strathcona Residents Association (residents-neighborhood-leaders), Vancouver Public Library (schools-libraries-community-centers), Carnegie Community Centre (schools-libraries-community-centers).
- Melbourne: integrated; imported 31; excluded 5; excluded leads: BeachPatrol Australia and Love Our Street (environmental-resilience-organizations), City of Melbourne (local-government-public-agencies), Emergency Management Victoria (local-government-public-agencies), City of Melbourne Libraries Makerspaces and Tool Library (makerspaces-tool-libraries-repair-groups), City of Melbourne Libraries (schools-libraries-community-centers).
- Perth: integrated; imported 25; excluded 3; excluded leads: Good Sammy Enterprises (local-businesses-social-enterprises), Perth Homeless Support Group Inc. (mutual-aid-groups), State Library of Western Australia (schools-libraries-community-centers).
- Sydney: integrated; imported 23; excluded 2; excluded leads: OzHarvest (direct-service-providers), Unions NSW (labor-unions-worker-centers).
- BWB South Afrika: repaired but not integrated in this checkpoint; replaced the malformed `research/completed/south africa.txt` source with `research/completed/deep-research-report-south-afrika.md`, normalized 26 importable opportunities, excluded The MakerSpace and Isivivana Centre into validation exclusions, and confirmed the remaining 26 opportunity websites pass the website validation gate.
