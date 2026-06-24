# Collaboration Opportunities for BWB Portland

## Summary

The strongest collaboration pattern for BWB Portland is **hands-on civic making**: Portland already has credible local infrastructure for participatory placemaking, creative reuse, volunteer build days, repair education, and tool sharing. City Repair’s Village Building Convergence, SCRAP’s creative-reuse programming, ReBuilding Center’s reuse-and-repair model, Northeast Portland Tool Library’s lending program, and Repair PDX’s repair cafés all align well with a Burner-adjacent chapter that can mobilize volunteers, salvage materials, and make practical public-facing projects feel welcoming rather than bureaucratic. citeturn30view0turn25view1turn26view5turn26view4turn26view3

A second strong pattern is **low-barrier mutual aid and direct service support**. Oregon Food Bank has volunteer pathways both at its Portland site and through partner agencies; Blanchet House and Rose Haven both expose concrete needs around meals, clothing, hygiene, and day-shelter support; Portland Mutual Aid Network and PDX Free Fridge offer flexible, fast-moving mutual-aid infrastructure; and APANO and Hacienda CDC add trusted neighborhood relationships in East Portland and the Cully/Jade District areas. That makes Portland especially suitable for collaborations built around supply sorting, hygiene kits, food redistribution, neighborhood resource fairs, and co-designed service days rather than generic “volunteer outreach.” citeturn30view3turn25view4turn25view5turn27view7turn27view8turn27view2turn26view8

A third pattern is that Portland has unusually plausible **formal civic pathways** for an informal chapter, but those pathways will often work best if BWB Portland partners through an established nonprofit or neighborhood intermediary. The Portland Bureau of Emergency Management offers free NET training; Portland Parks & Recreation has stewardship and public-programming infrastructure; District Coalition Offices explicitly provide neighborhood support and, in some cases, fiscal sponsorship or grants; and Oregon Community Foundation’s grant guidance makes clear that fiscally sponsored projects can apply where eligible. In practice, that means the most actionable route is often: neighborhood or community-based host + BWB volunteer energy + a modest grant or sponsorship layer. citeturn26view0turn26view1turn28view3turn35view0turn29view0turn29view1

## Opportunities

Portland’s best leads are not just “nice organizations.” They are organizations with **specific existing programs, facilities, volunteer systems, or neighborhood networks** that a BWB chapter could plug into quickly. East Portland is especially rich in place-based collaboration leads because APANO, Hacienda CDC, Green Lents, neighborhood coalitions, and several tool-sharing or food-distribution systems are all already operating there with public-facing programs. citeturn29view7turn26view8turn31view0turn27view0turn35view0

The YAML below is structured to be copy-friendly for a maintainer. I prioritized organizations with active public websites, explicit programs or volunteer opportunities, and a credible fit with arts/culture activation, mutual aid, direct service, resilience, neighborhood stewardship, and volunteer mobilization. Where a lead depends on geography, grant timing, or fiscal-sponsorship eligibility, that is called out in `research_notes`. citeturn25view0turn25view1turn30view3turn26view0turn27view6turn27view4

```yaml
opportunities:
  # arts-culture-organizations
  - opportunity_slug: city-repair-project
    organization_name: The City Repair Project
    category_slug: arts-culture-organizations
    status: research-lead
    website: https://cityrepair.org/
    why_it_may_fit: City Repair is one of Portland's clearest fits for participatory placemaking. Its annual Village Building Convergence centers neighbors, groups, and civic partnerships in transforming city spaces, and the organization publicly notes that it can support aligned programs under its nonprofit umbrella.
    possible_collaboration_shapes:
      - Co-host a neighborhood placemaking or street-activation build day tied to Village Building Convergence.
      - Explore whether a BWB-led public-space pilot could be incubated or advised through City Repair's aligned-project infrastructure.
    source_urls:
      - https://cityrepair.org/
      - https://cityrepair.org/village-building-convergence
      - https://cityrepair.org/programs
    research_notes: Verify the current VBC calendar, permit assumptions, and whether any proposed BWB project would qualify for City Repair's alignment-based support.
    last_verified: 2026-06-24

  - opportunity_slug: scrap-creative-reuse
    organization_name: SCRAP Creative Reuse
    category_slug: arts-culture-organizations
    status: research-lead
    website: https://scrappdx.org/
    why_it_may_fit: SCRAP combines affordable creative materials, volunteer pathways, and educational programming in a way that maps well to Burner-style build culture. It is an unusually practical bridge between arts activation and material reuse.
    possible_collaboration_shapes:
      - Run a community art-supply collection and redistribution drive for neighborhood activation projects.
      - Co-host creative-reuse workshops that pair art-making with repair, recycling, or resilience themes.
    source_urls:
      - https://scrappdx.org/
    research_notes: Confirm current donation acceptance rules, bulk-material handling, and whether group volunteer days can be scheduled for a chapter team.
    last_verified: 2026-06-24

  # direct-service-providers
  - opportunity_slug: oregon-food-bank
    organization_name: Oregon Food Bank
    category_slug: direct-service-providers
    status: research-lead
    website: https://www.oregonfoodbank.org/
    why_it_may_fit: Oregon Food Bank offers both Portland-site volunteering and opportunities through community partner organizations. That makes it a strong operational partner for supply sorting, food packing, neighborhood distributions, and volunteer mobilization that needs a real intake-and-distribution backbone.
    possible_collaboration_shapes:
      - Schedule recurring BWB sorting and repacking shifts at Oregon Food Bank's Portland location.
      - Pair BWB volunteers with a local pantry or distribution partner for seasonal food and essentials support.
    source_urls:
      - https://www.oregonfoodbank.org/
      - https://www.oregonfoodbank.org/get-involved/volunteer
    research_notes: Verify whether BWB wants warehouse-style volunteer shifts, partner-agency support, advocacy-oriented volunteering, or small-group opportunities.
    last_verified: 2026-06-24

  - opportunity_slug: blanchet-house
    organization_name: Blanchet House
    category_slug: direct-service-providers
    status: research-lead
    website: https://blanchethouse.org/
    why_it_may_fit: Blanchet House publicly highlights practical volunteer work such as serving meals, sorting clothing, and assembling care items. It is a good fit for short-cycle, concrete BWB service days with visible immediate outputs.
    possible_collaboration_shapes:
      - Organize a BWB meal-service volunteer day or small recurring meal-support team.
      - Build and deliver toiletry kits, sack lunches, or seasonal essentials matched to Blanchet House needs.
    source_urls:
      - https://blanchethouse.org/
    research_notes: Confirm current group-volunteer capacity and whether the most useful collaboration is meal service, clothing sorting, or home-based kit assembly.
    last_verified: 2026-06-24

  - opportunity_slug: rose-haven
    organization_name: Rose Haven
    category_slug: direct-service-providers
    status: research-lead
    website: https://rosehaven.org/
    why_it_may_fit: Rose Haven is Portland's day shelter and community center focused on women, children, and gender-diverse people, with publicly listed services including hospitality, laundry, supplies, showers, classes, and advocacy. That makes it a strong lead for dignity-centered hygiene and stabilization support.
    possible_collaboration_shapes:
      - Run a guest-informed hygiene and supplies drive matched to Rose Haven distribution priorities.
      - Offer volunteer help for classes, resource days, or hospitality support where Rose Haven staff identify a gap.
    source_urls:
      - https://rosehaven.org/services/
    research_notes: This is a population-specific service environment; outreach should be trauma-informed, low-ego, and led by Rose Haven's stated operational needs.
    last_verified: 2026-06-24

  # environmental-resilience-organizations
  - opportunity_slug: depave
    organization_name: Depave
    category_slug: environmental-resilience-organizations
    status: research-lead
    website: https://www.depave.org/
    why_it_may_fit: Depave is based in Portland and focuses on urban re-greening, climate adaptation, and underserved areas, working with schools, social-service organizations, and community-focused businesses. It is a strong fit for labor-intensive volunteer days that turn hardscape into community-serving green infrastructure.
    possible_collaboration_shapes:
      - Join or support a depaving and re-greening workday on a community-serving site.
      - Help prototype a small resilience project centered on shade, stormwater, seating, and neighborhood gathering space.
    source_urls:
      - https://www.depave.org/
      - https://www.depave.org/projects
    research_notes: Depave projects are site-specific and can involve longer planning horizons than a typical volunteer day; confirm whether there is an upcoming Portland project suited to episodic volunteers.
    last_verified: 2026-06-24

  - opportunity_slug: solve
    organization_name: SOLVE
    category_slug: environmental-resilience-organizations
    status: research-lead
    website: https://www.solve.org/
    why_it_may_fit: SOLVE already recruits and guides volunteers for cleanup and restoration events, and it explicitly allows groups to attend scheduled events or create their own. That makes it one of the cleanest ways for BWB Portland to plug into visible stewardship work quickly.
    possible_collaboration_shapes:
      - Adopt a recurring neighborhood or downtown cleanup under the SOLVE event framework.
      - Use SOLVE as the logistics backbone for a BWB-led cleanup that also includes art, outreach, or reuse elements.
    source_urls:
      - https://www.solve.org/
      - https://www.solveoregon.org/volunteer
    research_notes: Verify whether current Portland-area events or host-your-own cleanup pathways are the better fit for a chapter-led collaboration.
    last_verified: 2026-06-24

  # funders-fiscal-sponsors
  - opportunity_slug: oregon-community-foundation
    organization_name: Oregon Community Foundation
    category_slug: funders-fiscal-sponsors
    status: research-lead
    website: https://oregoncf.org/
    why_it_may_fit: OCF is a major Oregon funder with a community grants program that provides flexible funding, and its public grant guidance explicitly addresses fiscally sponsored applicants. For an informal chapter, this is a strong lead when paired with a qualified local sponsor or host organization.
    possible_collaboration_shapes:
      - Pursue flexible community-grant support for a neighborhood resilience, food-support, or civic-activation pilot.
      - Use OCF's public guidance to structure a fiscally sponsored application with a trusted Portland-area host.
    source_urls:
      - https://oregoncf.org/grants-and-scholarships/grants/community-grant-program
      - https://oregoncf.org/grants-and-scholarships/grants-resources
    research_notes: OCF cycles and eligibility shift over time; a BWB chapter would likely need a formal fiscal sponsor or nonprofit partner before applying.
    last_verified: 2026-06-24

  - opportunity_slug: southeast-uplift-neighborhood-coalition
    organization_name: Southeast Uplift Neighborhood Coalition
    category_slug: funders-fiscal-sponsors
    status: research-lead
    website: https://www.seuplift.org/
    why_it_may_fit: Southeast Uplift is a City-supported District Coalition Office, and public SE Uplift materials describe an active fiscal-sponsorship program that provides bookkeeping, training, and administrative support for grassroots organizations. That makes it one of the more concrete local options for a neighborhood-rooted BWB pilot that needs 501(c)(3) infrastructure.
    possible_collaboration_shapes:
      - Explore fiscal sponsorship for a Southeast or inner Northeast Portland community project with clear resident backing.
      - Pair fiscal sponsorship with neighborhood outreach and community-small-grants preparation for a co-designed pilot.
    source_urls:
      - https://www.portland.gov/civic/dco-model-updates
      - https://www.seuplift.org/wp-content/uploads/2024/04/Fiscal-Sponsorship-Program-Guide-FY24-25.pdf
    research_notes: Geography matters here; verify service boundaries, eligibility, fees, and whether SE Uplift currently sponsors non-neighborhood groups or only projects aligned with specific neighborhood structures.
    last_verified: 2026-06-24

  # labor-unions-worker-centers
  - opportunity_slug: portland-jobs-with-justice
    organization_name: Portland Jobs with Justice
    category_slug: labor-unions-worker-centers
    status: research-lead
    website: https://jwjpdx.org/
    why_it_may_fit: Portland Jobs with Justice is a long-running labor-community coalition that publicly says it includes more than 100 labor, community, student, and allied organizations. It is a credible bridge for worker-centered resource events, community solidarity work, and volunteer recruitment through trusted movement networks.
    possible_collaboration_shapes:
      - Co-host a worker-resource or solidarity event that combines material aid with labor-community organizing.
      - Recruit labor-community volunteers for a build day, emergency-support action, or neighborhood mutual-aid project.
    source_urls:
      - https://jwjpdx.org/
    research_notes: Best fit is likely coalition work, turnout, and worker-centered framing rather than technical build support.
    last_verified: 2026-06-24

  - opportunity_slug: ibew-local-48
    organization_name: IBEW Local 48
    category_slug: labor-unions-worker-centers
    status: research-lead
    website: https://www.ibew48.com/
    why_it_may_fit: IBEW Local 48 publicly highlights ongoing education and training, a large regional membership base, and member volunteer involvement outside the jobsite. It is a strong lead when a project needs skilled-trades insight, safety culture, or a formal labor partner for infrastructure-heavy work.
    possible_collaboration_shapes:
      - Ask about skilled-volunteer or advisory support for safe temporary power, lighting, or event-infrastructure planning.
      - Co-host a safety-oriented workshop on build practices, jobsite culture, or volunteer risk reduction.
    source_urls:
      - https://www.ibew48.com/
      - https://www.ibew48.com/members/get-involved/
    research_notes: Any actual trade work would need careful scope, liability, and jurisdiction review; this is a better fit for sanctioned support than informal volunteer improvisation.
    last_verified: 2026-06-24

  # local-businesses-social-enterprises
  - opportunity_slug: rebuilding-center
    organization_name: ReBuilding Center
    category_slug: local-businesses-social-enterprises
    status: research-lead
    website: https://www.rebuildingcenter.org/
    why_it_may_fit: ReBuilding Center combines a reuse store, repair classes, volunteer opportunities, group team-building formats, and material donation intake. It is an unusually strong match for BWB-style build culture that wants to source materials, teach practical skills, and reduce waste at the same time.
    possible_collaboration_shapes:
      - Source reused materials for community build projects or resilience infrastructure experiments.
      - Co-host a repair or build-skills day using ReBuilding Center instructors, volunteers, or class formats.
    source_urls:
      - https://www.rebuildingcenter.org/
      - https://www.rebuildingcenter.org/volunteer
      - https://www.rebuildingcenter.org/group-teams
    research_notes: Verify whether the better entry point is donations, volunteer teams, classes, or community outreach support for grassroots projects.
    last_verified: 2026-06-24

  - opportunity_slug: free-geek
    organization_name: Free Geek
    category_slug: local-businesses-social-enterprises
    status: research-lead
    website: https://www.freegeek.org/
    why_it_may_fit: Free Geek's public mission pairs sustainable technology reuse with digital access and education, and it offers both volunteer opportunities and community technology pathways. It is a strong lead for projects that blend mutual aid, digital inclusion, and reuse.
    possible_collaboration_shapes:
      - Run a community tech-collection and refurbishment drive tied to a local nonprofit or neighborhood need.
      - Add device access, digital-literacy support, or computer referral pathways to a BWB resource fair or resilience-hub concept.
    source_urls:
      - https://www.freegeek.org/
      - https://www.freegeek.org/what-we-do/digital-access
      - https://www.freegeek.org/take-action-donate-technology/volunteer
    research_notes: Confirm current volunteer capacity, nonprofit-device eligibility rules, and whether program operations are shifting because of the organization's announced 2026 move.
    last_verified: 2026-06-24

  # local-government-public-agencies
  - opportunity_slug: portland-bureau-of-emergency-management
    organization_name: Portland Bureau of Emergency Management
    category_slug: local-government-public-agencies
    status: research-lead
    website: https://www.portland.gov/pbem
    why_it_may_fit: PBEM is one of the most concrete public-agency fits for BWB Portland because it offers free Neighborhood Emergency Team training for people who live or work in Portland and maintains a large active volunteer base. That creates a direct bridge into neighborhood preparedness and response culture.
    possible_collaboration_shapes:
      - Encourage BWB members to complete NET training and then co-host neighborhood preparedness workshops.
      - Partner on public-facing emergency-readiness events, supply-prep sessions, or resilience communications.
    source_urls:
      - https://www.portland.gov/pbem
      - https://www.portland.gov/pbem/neighborhood-emergency-teams/volunteer
    research_notes: Best fit is preparedness, training, and neighborhood readiness rather than front-line emergency operations.
    last_verified: 2026-06-24

  - opportunity_slug: portland-parks-and-recreation
    organization_name: Portland Parks & Recreation
    category_slug: local-government-public-agencies
    status: research-lead
    website: https://www.portland.gov/parks
    why_it_may_fit: PP&R already operates natural-area stewardship, community gardens, arts-and-culture programming, recreation, and citywide community facilities. It is a practical route for park cleanups, stewardship days, outdoor civic art, and neighborhood-facing public programming.
    possible_collaboration_shapes:
      - Co-host a stewardship day or cleanup in a park or natural area with a visible volunteer component.
      - Pair a park-based service action with a free public workshop, art activity, or resilience demonstration.
    source_urls:
      - https://www.portland.gov/parks
    research_notes: Verify permit, insurance, and site-selection requirements early; bureau partnership is likely easier for clearly scoped public-space projects than for loosely defined events.
    last_verified: 2026-06-24

  # makerspaces-tool-libraries-repair-groups
  - opportunity_slug: northeast-portland-tool-library
    organization_name: Northeast Portland Tool Library
    category_slug: makerspaces-tool-libraries-repair-groups
    status: research-lead
    website: https://www.neptl.org/
    why_it_may_fit: NEPTL provides tool access to residents of all income levels and explicitly offers membership, volunteering, and group-loan pathways. That gives BWB a practical infrastructure partner for neighborhood build days that need tools more than funding.
    possible_collaboration_shapes:
      - Borrow tools through group-loan pathways for a neighborhood repair or beautification day.
      - Co-host a volunteer build event that demonstrates tool sharing and low-cost maintenance skills.
    source_urls:
      - https://www.neptl.org/
    research_notes: Confirm whether a BWB-led event qualifies for group loans and whether non-neighborhood participants need a local host or member sponsor.
    last_verified: 2026-06-24

  - opportunity_slug: repair-pdx
    organization_name: Repair PDX
    category_slug: makerspaces-tool-libraries-repair-groups
    status: research-lead
    website: https://www.repairpdx.org/
    why_it_may_fit: Repair PDX has organized free Repair Cafés since 2013 and is expanding repair-education programming with workshops. This is one of the cleanest Portland fits for a BWB chapter that wants a practical, public-serving “fix things together” collaboration.
    possible_collaboration_shapes:
      - Co-host a Repair Café for neighbors alongside a mutual-aid or resource-sharing event.
      - Add repair education to a broader BWB sustainability or emergency-readiness workshop series.
    source_urls:
      - https://www.repairpdx.org/
      - https://www.repairpdx.org/repair-events
    research_notes: Verify event calendar cadence, needed volunteer skill mix, and whether Repair PDX prefers to lead, co-brand, or simply advise local repair events.
    last_verified: 2026-06-24

  - opportunity_slug: green-lents-community-tool-library
    organization_name: Green Lents Community Tool Library
    category_slug: makerspaces-tool-libraries-repair-groups
    status: research-lead
    website: https://www.greenlents.org/tool-library
    why_it_may_fit: Green Lents' tool library is fully volunteer-run, explicitly focused on accessibility, community, and skill building, and serves a wide swath of SE and East Portland neighborhoods. It is especially promising for neighborhood-rooted work in East Portland.
    possible_collaboration_shapes:
      - Organize an East Portland build or repair day using Green Lents tool access and local volunteer channels.
      - Pair a small infrastructure project with a free maintenance or bike-repair workshop in the Green Lents footprint.
    source_urls:
      - https://www.greenlents.org/
      - https://www.greenlents.org/tool-library
    research_notes: Service area is geographically bounded; confirm that any proposed project sits inside the library's lending footprint or has a local member/host pathway.
    last_verified: 2026-06-24

  # mutual-aid-groups
  - opportunity_slug: portland-mutual-aid-network
    organization_name: Portland Mutual Aid Network
    category_slug: mutual-aid-groups
    status: research-lead
    website: https://portlandmutualaidnetwork.com/
    why_it_may_fit: Portland Mutual Aid Network is an all-volunteer group that publicly describes weekly distribution of food, survival supplies, and personal-care products shaped by the needs of unhoused Portlanders. It is a strong lead for fast, low-overhead collaboration around immediate material support.
    possible_collaboration_shapes:
      - Contribute volunteers and supplies to an existing weekly distribution rather than creating a parallel effort.
      - Coordinate a one-off or seasonal supply drive around the specific categories PMAN already moves regularly.
    source_urls:
      - https://portlandmutualaidnetwork.com/
    research_notes: This is a mutual-aid environment rather than a traditional service-provider partnership; approach should respect PMAN's own political framing and distribution rhythm.
    last_verified: 2026-06-24

  - opportunity_slug: pdx-free-fridge
    organization_name: PDX Free Fridge
    category_slug: mutual-aid-groups
    status: research-lead
    website: https://sites.google.com/view/pdx-free-fridge/home
    why_it_may_fit: PDX Free Fridge maintains a decentralized network of independent fridges and pantries across Portland and explicitly provides community guidelines, startup guidance, and a public map. It is a strong fit for low-barrier food and essentials redistribution.
    possible_collaboration_shapes:
      - Adopt regular stocking support for one or more fridges or pantries in a targeted neighborhood.
      - Use BWB volunteers to build, repair, paint, or weatherize fridge/pantry enclosures where local hosts want help.
    source_urls:
      - https://sites.google.com/view/pdx-free-fridge/home
    research_notes: Because the network is decentralized and not nonprofit-run, verify which site hosts actually want outside volunteer help before launching a public drive or build.
    last_verified: 2026-06-24

  # nonprofits-cbos
  - opportunity_slug: apano
    organization_name: APANO
    category_slug: nonprofits-cbos
    status: research-lead
    website: https://apano.org/
    why_it_may_fit: APANO combines community development, cultural work, organizing, small-business support, and concrete volunteer opportunities such as Jade District food-distribution support. For BWB Portland, it is one of the strongest East Portland leads for co-designed, neighborhood-trusted civic work.
    possible_collaboration_shapes:
      - Support APANO's Free Food Market or another neighborhood-serving event with volunteers, setup, and material logistics.
      - Co-develop a Jade District or Orchards-area placemaking, resource-fair, or resilience project with local cultural grounding.
    source_urls:
      - https://www.apano.org/about/about
      - https://www.apano.org/our-work/cultural-work-portfolio/creative-placekeeping
      - https://www.apano.org/our-work/jade-district
      - https://www.apano.org/get-involved/volunteers/freefoodmarkethelper
    research_notes: Best fit is likely East Portland and community-led work; verify that any proposed collaboration is requested by APANO staff or neighborhood partners rather than imported from outside.
    last_verified: 2026-06-24

  - opportunity_slug: hacienda-cdc
    organization_name: Hacienda CDC
    category_slug: nonprofits-cbos
    status: research-lead
    website: https://www.haciendacdc.org/
    why_it_may_fit: Hacienda CDC is a trusted Latino-led housing and community-development organization with resident services, youth and family programming, volunteer pathways, and community spaces. It is a strong lead for resident-centered events, family support, and neighborhood-rooted activation in the Cully area and beyond.
    possible_collaboration_shapes:
      - Support a resident-focused resource fair, volunteer day, or family event at a Hacienda community space.
      - Coordinate in-kind donations, setup help, or volunteer logistics for Hacienda-led resident services or youth-and-family programming.
    source_urls:
      - https://www.haciendacdc.org/about-us
      - https://www.haciendacdc.org/volunteer
    research_notes: Verify which Hacienda site, program team, or community space is the best fit before outreach; needs may differ across housing, youth, and resident-services teams.
    last_verified: 2026-06-24

  # residents-neighborhood-leaders
  - opportunity_slug: northeast-coalition-of-neighborhoods
    organization_name: Northeast Coalition of Neighborhoods
    category_slug: residents-neighborhood-leaders
    status: research-lead
    website: https://www.necoalition.org/
    why_it_may_fit: NECN is a resident-facing District 2 coalition that helps North and Northeast Portland neighbors identify local issues, engage land-use processes, and access grants and neighborhood-association infrastructure. It is a practical route to real neighborhood leadership rather than generic outreach.
    possible_collaboration_shapes:
      - Convene listening sessions with neighborhood association leaders before designing a local project.
      - Identify a small community-strengthening project that BWB volunteers can support under neighborhood guidance.
    source_urls:
      - https://www.necoalition.org/
      - https://www.necoalition.org/about-us
      - https://www.necoalition.org/grants
    research_notes: NECN itself is an intermediary, not the end community; outreach should ask which specific neighborhood associations or resident groups want support.
    last_verified: 2026-06-24

  - opportunity_slug: district-four-coalition
    organization_name: District Four Coalition
    category_slug: residents-neighborhood-leaders
    status: research-lead
    website: https://districtfourcoalition.org/
    why_it_may_fit: District Four Coalition represents a large alliance of neighborhood associations across NW, SW, downtown, and parts of inner Southeast Portland, and publicly offers grants, training, emergency-prep resources, and get-involved pathways. It is a useful route into resident leadership where BWB wants co-designed neighborhood work instead of top-down project selection.
    possible_collaboration_shapes:
      - Bring a project idea to D4C as a resident-informed concept and ask which neighborhood associations want to shape it.
      - Support a neighborhood-led cleanup, emergency-prep event, or small livability project in District 4 with volunteer labor and materials.
    source_urls:
      - https://districtfourcoalition.org/
      - https://districtfourcoalition.org/about/
      - https://districtfourcoalition.org/programs-and-services/programs/land-use-and-transportation/
    research_notes: D4C covers a very large and diverse footprint; ask for the best neighborhood-level entry point rather than treating the district as a single community.
    last_verified: 2026-06-24

  # schools-libraries-community-centers
  - opportunity_slug: multnomah-county-library
    organization_name: Multnomah County Library
    category_slug: schools-libraries-community-centers
    status: research-lead
    website: https://multcolib.org/
    why_it_may_fit: Multnomah County Library offers free community-room use for educational, cultural, civic, and recreational purposes and also maintains a volunteer program. That gives BWB Portland a legitimate public venue pathway for workshops, repair clinics, preparedness sessions, and small civic events.
    possible_collaboration_shapes:
      - Host a free public workshop or repair/preparedness session in an approved library community room.
      - Work with library staff on volunteer-supported civic or family programming with a practical skills focus.
    source_urls:
      - https://multcolib.org/community-rooms
      - https://multcolib.org/volunteer
    research_notes: Large community rooms require approval and public-open access; verify room-application timelines and which branches are best for the target neighborhood.
    last_verified: 2026-06-24

  - opportunity_slug: portland-community-college-community-based-learning
    organization_name: Portland Community College Community-Based Learning
    category_slug: schools-libraries-community-centers
    status: research-lead
    website: https://www.pcc.edu/community-based-learning/
    why_it_may_fit: PCC's Community-Based Learning program supports community-based work across disciplines and connects students to hands-on volunteering throughout the greater Portland region. It is a strong lead if BWB Portland wants project-based student volunteers, class-linked service, or skilled support from a community-college setting.
    possible_collaboration_shapes:
      - Offer a defined volunteer or service-learning project that PCC students can join through community-based learning channels.
      - Co-design a short-term civic project with faculty or program staff that includes reflection, practical service, and neighborhood benefit.
    source_urls:
      - https://www.pcc.edu/community-based-learning/
    research_notes: PCC collaboration will likely work best if the project scope is clear, semester-friendly, and suitable for faculty or student approval processes.
    last_verified: 2026-06-24
```

## No good leads found

```yaml
no_good_leads_found: []
```

## Follow-up questions

```yaml
follow_up_questions:
  - Should BWB Portland prioritize citywide chapters-scale collaborations, or is it more useful to focus on one geography such as East Portland, North/Northeast Portland, or the central city?
  - Is the chapter willing to work through a fiscal sponsor or host nonprofit for grants, insurance, and compliance if a project grows beyond informal volunteer action?
  - Which collaboration mode is most realistic for the chapter over the next year: direct service, public-space stewardship, preparedness training, creative placemaking, repair/reuse, or neighborhood listening?
  - Does the chapter want recurring volunteer placements with existing organizations, or mostly one-off co-branded public events and build days?
  - Are there existing relationships with Portland regional burners, maker crews, neighborhood associations, or nonprofit partners that would make one cluster of leads easier to activate first?
  - For direct-service partnerships, does the chapter want low-barrier supply and logistics support, or is it prepared for regular relationship-based volunteer commitments?
  - For public-agency or neighborhood-coalition outreach, who in the chapter can reliably handle permitting, scheduling, and follow-through after an introductory meeting?
```

## Source index

```yaml
source_index:
  - url: https://cityrepair.org/
    note: City Repair overview and programs page supporting placemaking fit and aligned-project support.
  - url: https://cityrepair.org/village-building-convergence
    note: Supports Village Building Convergence as an annual collaboration among neighbors, groups, and civic partners.
  - url: https://cityrepair.org/programs
    note: Supports City Repair program structure and VBC positioning.

  - url: https://scrappdx.org/
    note: Supports SCRAP's mission, educational programming, volunteer pathways, and creative-reuse center.

  - url: https://www.oregonfoodbank.org/
    note: Supports Oregon Food Bank's regional food-distribution network.
  - url: https://www.oregonfoodbank.org/get-involved/volunteer
    note: Supports Portland-site and partner-based volunteer opportunities.

  - url: https://blanchethouse.org/
    note: Supports Blanchet House's volunteer and direct-service relevance.

  - url: https://rosehaven.org/services/
    note: Supports Rose Haven's day-shelter functions and listed services such as supplies, showers, laundry, and classes.

  - url: https://www.depave.org/
    note: Supports Depave's mission around re-greening and climate adaptation.
  - url: https://www.depave.org/projects
    note: Supports Depave's Portland base and collaboration with community partners on underserved sites.

  - url: https://www.solve.org/
    note: Supports SOLVE's current Oregon cleanup and volunteer infrastructure.
  - url: https://www.solveoregon.org/volunteer
    note: Supports group and host-your-own volunteer pathways.

  - url: https://oregoncf.org/grants-and-scholarships/grants/community-grant-program
    note: Supports Oregon Community Foundation's flexible Community Grants program and cycle structure.
  - url: https://oregoncf.org/grants-and-scholarships/grants-resources
    note: Supports OCF guidance on fiscally sponsored applicants.

  - url: https://www.portland.gov/civic/dco-model-updates
    note: Supports Portland's District Coalition Office model and the role of DCOs in neighborhood support and fiscal sponsorship.
  - url: https://www.seuplift.org/wp-content/uploads/2024/04/Fiscal-Sponsorship-Program-Guide-FY24-25.pdf
    note: Supports SE Uplift's public fiscal-sponsorship program materials and grassroots-support role.

  - url: https://jwjpdx.org/
    note: Supports Portland Jobs with Justice as a labor-community coalition.

  - url: https://www.ibew48.com/
    note: Supports IBEW Local 48's training base, membership scale, and volunteer-facing member involvement.
  - url: https://www.ibew48.com/members/get-involved/
    note: Supports explicit Local 48 volunteer and committee participation pathways.

  - url: https://www.rebuildingcenter.org/
    note: Supports ReBuilding Center's reuse store, classes, events, and social-enterprise model.
  - url: https://www.rebuildingcenter.org/volunteer
    note: Supports volunteer pathways at ReBuilding Center.
  - url: https://www.rebuildingcenter.org/group-teams
    note: Supports group classes and volunteering for teams.

  - url: https://www.freegeek.org/
    note: Supports Free Geek's mission around technology reuse, digital access, and education.
  - url: https://www.freegeek.org/what-we-do/digital-access
    note: Supports device-refurbishment and community-program pathways.
  - url: https://www.freegeek.org/take-action-donate-technology/volunteer
    note: Supports current Free Geek volunteer opportunities.

  - url: https://www.portland.gov/pbem
    note: Supports PBEM as the relevant city emergency-management bureau.
  - url: https://www.portland.gov/pbem/neighborhood-emergency-teams/volunteer
    note: Supports free NET training and active-volunteer claims.

  - url: https://www.portland.gov/parks
    note: Supports PP&R's public programs, stewardship, arts/culture, and community-facing infrastructure.

  - url: https://www.neptl.org/
    note: Supports Northeast Portland Tool Library's mission, membership, volunteer, and group-loan pathways.

  - url: https://www.repairpdx.org/
    note: Supports Repair PDX's repair-café model and repair-education mission.
  - url: https://www.repairpdx.org/repair-events
    note: Supports Repair PDX's event framing and public calendar.

  - url: https://www.greenlents.org/
    note: Supports Green Lents' mission around social and environmental resilience.
  - url: https://www.greenlents.org/tool-library
    note: Supports the Green Lents Community Tool Library's service area, volunteer structure, and workshop activity.

  - url: https://portlandmutualaidnetwork.com/
    note: Supports Portland Mutual Aid Network's weekly all-volunteer distribution model.

  - url: https://sites.google.com/view/pdx-free-fridge/home
    note: Supports PDX Free Fridge's decentralized network, public map, and startup guidance.

  - url: https://www.apano.org/about/about
    note: Supports APANO's mission and community-development role.
  - url: https://www.apano.org/our-work/cultural-work-portfolio/creative-placekeeping
    note: Supports APANO's creative-placekeeping work in the Jade District and greater East Portland.
  - url: https://www.apano.org/our-work/jade-district
    note: Supports APANO's place-based Jade District work.
  - url: https://www.apano.org/get-involved/volunteers/freefoodmarkethelper
    note: Supports APANO's volunteer-facing Free Food Market work.

  - url: https://www.haciendacdc.org/about-us
    note: Supports Hacienda CDC's resident-centered services and Portland-area role.
  - url: https://www.haciendacdc.org/volunteer
    note: Supports Hacienda CDC's public volunteer pathways.

  - url: https://www.necoalition.org/
    note: Supports NECN's district role and neighborhood-association network.
  - url: https://www.necoalition.org/about-us
    note: Supports NECN's mission and resident-engagement framing.
  - url: https://www.necoalition.org/grants
    note: Supports NECN's community-grant infrastructure.

  - url: https://districtfourcoalition.org/
    note: Supports District Four Coalition's neighborhood coverage, programs, and public get-involved pathways.
  - url: https://districtfourcoalition.org/about/
    note: Supports D4C's representation of 32 neighborhood associations and district coverage.
  - url: https://districtfourcoalition.org/programs-and-services/programs/land-use-and-transportation/
    note: Supports D4C's resident-guidance and civic-navigation role.

  - url: https://multcolib.org/community-rooms
    note: Supports Multnomah County Library's free community-room program and public-use requirements.
  - url: https://multcolib.org/volunteer
    note: Supports Multnomah County Library's volunteer program.

  - url: https://www.pcc.edu/community-based-learning/
    note: Supports PCC's Community-Based Learning program and region-wide volunteering infrastructure.
```