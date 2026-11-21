# Expert Roster: Advisory Agent Team

This is the expert team a consultant would want around them for the **Miami specialty coffee shop** project. It is built from the research in this folder ([README](README.md)). Each role below is meant to become one agent. Skills are defined once and shared, so several agents can use the same skill.

- **31 agents** in 11 domains, plus **38 shared skills**.
- **Tier:** *Core* agents should be built first and take part in most decisions. *On-demand* agents are called in for specialist questions.
- **Key docs** are the research files each agent should load as context (01 = `01-market.md`, and so on).
- `agent-id` and `skill-id` values are written as slugs so they can be used directly as file names, such as `.claude/agents/<agent-id>.md` and `.claude/skills/<skill-id>/SKILL.md`.

## 1. Expert agents


### Leadership

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 1 | **Engagement Lead (orchestrator)** | `engagement-lead` | Core | Runs the advisory team: routes questions to the right experts, combines their advice into recommendations, and keeps the decision log. | All |
| 2 | **Red Team Reviewer** | `red-team-reviewer` | Core | Challenges every major recommendation by testing assumptions, running downside cases and checking sources before advice reaches the client. | All, esp. 04, 08 |

### Business & strategy

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 3 | **Market & Strategy Analyst** | `market-strategist` | Core | Sizes the Miami specialty-coffee opportunity and turns market trends into a go/no-go case and a growth strategy. | 01, 02, 03 |
| 4 | **Customer Insights Researcher** | `customer-insights` | On-demand | Defines and validates the customer segments with demographics, bilingual surveys and foot-traffic counts. | 02 |
| 5 | **Competitive Intelligence Analyst** | `competitive-intel` | Core | Maps and monitors specialty roasters, ventanitas and chains around each candidate site, including their prices, formats and gaps. | 03 |
| 6 | **Concept & Format Strategist** | `concept-designer` | Core | Chooses the shop format and positioning (Cuban x specialty, cowork café, or grab-and-go) and sets the seat count and service model. | 02, 03, 07 |
| 7 | **Miami Culture & Localization Advisor** | `cultural-advisor` | On-demand | Makes sure the concept, menu, language and service fit Miami's bilingual, Cuban-rooted coffee culture. | 02, 03, 07 |

### Coffee & product

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 8 | **Specialty Coffee Director** | `head-of-coffee` | Core | Picks the roaster partner, sets recipes and quality standards, manages green-coffee price exposure, and leads barista craft. | 01, 03, 04, 08 |
| 9 | **Menu & Food Program Developer** | `menu-developer` | On-demand | Designs the drink and food menu and the price ladder ($3 Cuban espresso up to premium) while hitting COGS targets. | 03, 04 |

### Real estate & build

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 10 | **Site Selection & Real Estate Advisor** | `site-selection` | Core | Finds and scores candidate locations on traffic, rent plus NNN, parking, flood zone, zoning and competitor density. | 02, 03, 04, 08 |
| 11 | **Design & Buildout Project Manager** | `buildout-manager` | On-demand | Manages the architect, contractor and inspections so the space opens on schedule and within the buildout budget. | 04, 05, 08 |

### Technical

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 12 | **Coffee Equipment & Water Specialist** | `equipment-specialist` | On-demand | Specifies the espresso machine, grinders, water filtration and refrigeration, plus the power and plumbing they need and their service contracts. | 04, 08 |
| 13 | **Technology & POS Architect** | `tech-architect` | On-demand | Selects and integrates the POS, mobile ordering, loyalty, delivery, Wi-Fi and security systems. | 04, 07 |
| 14 | **Data & Performance Analyst** | `data-analyst` | On-demand | Builds the KPI dashboard and early-warning alerts (transactions, ticket, labor %, COGS %, cash runway, ratings). | 04, 08 |

### Operations

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 15 | **Operations Manager** | `operations-manager` | Core | Designs daily operations: SOPs, opening and closing, quality control, vendor flow and shift management. | 04, 06, 08 |
| 16 | **Supply Chain & Procurement Specialist** | `procurement` | On-demand | Sources and contracts coffee, milk, food, packaging and smallwares at the best total cost, and manages par levels. | 01, 04, 08 |
| 17 | **Food Safety & Health Compliance Officer** | `food-safety` | On-demand | Keeps the shop inspection-ready: DBPR standards, food-manager certification, staff food-safety training and logs. | 05, 06 |
| 18 | **Customer Experience & Hospitality Designer** | `cx-designer` | On-demand | Designs the customer journey (ventanita window, counter and seating), queue flow and hospitality standards. | 02, 07 |

### People

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 19 | **HR, Hiring & Training Lead** | `hr-talent` | Core | Hires, onboards, trains and keeps a bilingual team, with pay and culture that reduce barista turnover. | 06 |
| 20 | **Labor & Workforce Planner** | `workforce-planner` | On-demand | Models staffing and schedules against sales so labor stays at 28–35% of revenue under Florida's $15 minimum wage. | 04, 06 |

### Finance

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 21 | **Financial Planning & Analysis Lead** | `financial-modeler` | Core | Owns the startup budget, monthly P&L, 36-month cash-flow model, break-even and scenarios. | 04, 06, 08 |
| 22 | **Funding & Capital Advisor** | `funding-advisor` | On-demand | Structures the funding mix (savings, SBA 7(a) or microloan, equipment financing, investors) and prepares lender packages. | 04, 08 |
| 23 | **Accounting & Tax Advisor** | `tax-accountant` | On-demand | Sets up bookkeeping and payroll, and handles Florida sales tax (7% in Miami-Dade), reemployment tax and local tax receipts. | 04, 05, 06 |

### Legal

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 24 | **Business Formation & Contracts Counsel** | `corporate-counsel` | On-demand | Forms the entity and reviews supplier, contractor, equipment and partner contracts. | 05 |
| 25 | **Commercial Lease Counsel** | `lease-counsel` | Core | Negotiates and reviews the lease: NNN/CAM, TI allowance, free rent, permit contingency, personal guarantee and term. | 04, 05, 08 |
| 26 | **Permits & Licensing Expeditor** | `permits-expeditor` | Core | Identifies the jurisdiction and drives every permit to approval: zoning, CU, BTR, DBPR, DERM, sidewalk café and signage. | 05 |
| 27 | **Employment Law Advisor** | `employment-counsel` | On-demand | Keeps hiring and pay compliant: minimum and tipped wage, tip pools, E-Verify, workers' comp and required posters. | 06 |

### Marketing

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 28 | **Brand & Marketing Strategist** | `brand-strategist` | Core | Defines the brand, positioning and marketing plan and budget, tied to the target segments. | 02, 03, 07 |
| 29 | **Digital, Social & Reputation Marketer** | `digital-marketer` | On-demand | Runs bilingual Instagram and TikTok, the Google Business Profile, reviews, email/SMS and app-based loyalty campaigns. | 07 |
| 30 | **Community, PR & B2B Partnerships Manager** | `community-partnerships` | On-demand | Builds press, creator, event (Art Basel and others) and office/catering and wholesale partnerships. | 07 |

### Risk

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 31 | **Risk, Insurance & Business Continuity Advisor** | `risk-manager` | Core | Maintains the risk register, insurance program and hurricane plan, and watches the early-warning indicators. | 08, 04 |

## 2. Shared skills and the agents that use them

| # | `skill-id` | What the skill does | Used by | # agents |
|---|---|---|---|---|
| 1 | `docs-knowledge-base` | Read and update the `docs/` research pack, using the Fact / Estimate / Assumption / To-verify labels. | **All agents** | 31 |
| 2 | `cited-web-research` | Find current public information and cite every fact with a link and a date; flag stale or second-hand sources. | `market-strategist`, `customer-insights`, `competitive-intel`, `cultural-advisor`, `head-of-coffee`, `site-selection`, `equipment-specialist`, `tech-architect`, `procurement`, `food-safety`, `funding-advisor`, `tax-accountant`, `corporate-counsel`, `lease-counsel`, `permits-expeditor`, `employment-counsel`, `brand-strategist`, `community-partnerships`, `risk-manager`, `red-team-reviewer` | 20 |
| 3 | `miami-market-data` | Pull and interpret Census/ACS, County Business Patterns (NAICS 722515) and GMCVB visitor data for Miami-Dade neighborhoods. | `market-strategist`, `customer-insights`, `site-selection`, `data-analyst` | 4 |
| 4 | `competitor-mapping` | Map every coffee seller within a set radius and run a mystery-shop checklist (prices, ticket, queue, seats, busiest hours). | `competitive-intel`, `site-selection`, `concept-designer`, `menu-developer`, `brand-strategist` | 5 |
| 5 | `customer-research` | Design bilingual surveys and interviews, run foot-traffic counts, and build segment personas. | `customer-insights`, `site-selection`, `cx-designer`, `brand-strategist`, `cultural-advisor` | 5 |
| 6 | `bilingual-localization` | Write and review English/Spanish copy and Cuban coffee terms; check cultural fit. | `cultural-advisor`, `brand-strategist`, `digital-marketer`, `menu-developer`, `cx-designer`, `hr-talent`, `community-partnerships` | 7 |
| 7 | `concept-positioning` | Score format and positioning options (kiosk, café or roastery; Cuban x specialty, cowork, grab-and-go) against market, cost and risk. | `concept-designer`, `market-strategist`, `brand-strategist`, `financial-modeler`, `engagement-lead` | 5 |
| 8 | `site-scorecard` | Score candidate sites on traffic, rent plus NNN, parking, FEMA flood zone, zoning and competitor density. | `site-selection`, `competitive-intel`, `permits-expeditor`, `risk-manager`, `financial-modeler` | 5 |
| 9 | `lease-analysis` | Analyze lease terms: NNN/CAM, TI allowance, free rent, permit contingency, guarantee, term and occupancy cost as a % of revenue. | `lease-counsel`, `site-selection`, `financial-modeler`, `risk-manager` | 4 |
| 10 | `financial-modeling` | Build the startup budget, monthly P&L, 36-month cash flow, break-even and upside/downside scenarios. | `financial-modeler`, `funding-advisor`, `data-analyst`, `red-team-reviewer`, `engagement-lead` | 5 |
| 11 | `menu-costing-and-pricing` | Cost each menu item, build the price ladder, hold beverage COGS at 15–20%, and model price changes. | `menu-developer`, `head-of-coffee`, `procurement`, `financial-modeler`, `concept-designer` | 5 |
| 12 | `labor-modeling-and-scheduling` | Model coverage hours and labor cost under Florida wage law and build schedules from POS sales data. | `workforce-planner`, `hr-talent`, `operations-manager`, `financial-modeler`, `data-analyst` | 5 |
| 13 | `funding-packaging` | Prepare SBA 7(a) or microloan applications, lender packages and investor decks. | `funding-advisor`, `financial-modeler`, `corporate-counsel`, `engagement-lead` | 4 |
| 14 | `florida-tax-compliance` | Apply the 7% Miami-Dade sales tax, DR-15 filing, reemployment tax, local food-and-beverage or resort taxes and tax receipts; configure tax in the POS. | `tax-accountant`, `permits-expeditor`, `financial-modeler`, `tech-architect` | 4 |
| 15 | `permit-pathway` | Find which jurisdiction covers a site, list the required permits (CU, BTR, DBPR, DERM, sidewalk café, signs), put them in order and track them. | `permits-expeditor`, `buildout-manager`, `site-selection`, `food-safety`, `lease-counsel` | 5 |
| 16 | `food-safety-compliance` | Apply DBPR food-code standards, food-manager certification, staff training, inspection prep and temperature and cleaning logs. | `food-safety`, `operations-manager`, `hr-talent`, `menu-developer` | 4 |
| 17 | `employment-compliance-fl` | Apply the $15 minimum wage, $11.98 tipped wage, tip-pool rules, E-Verify (25+ employees), workers' comp and required posters. | `employment-counsel`, `hr-talent`, `workforce-planner`, `tax-accountant` | 4 |
| 18 | `contract-review` | Review supplier, roaster, equipment-lease, contractor and partnership contracts and flag risky terms. | `corporate-counsel`, `lease-counsel`, `procurement`, `head-of-coffee`, `equipment-specialist`, `buildout-manager`, `tech-architect` | 7 |
| 19 | `buildout-project-management` | Track the buildout schedule, budget, change orders, 10–30% overrun risk and inspection milestones. | `buildout-manager`, `permits-expeditor`, `equipment-specialist`, `financial-modeler` | 4 |
| 20 | `equipment-specification` | Specify the espresso machine, grinders, water filtration and refrigeration; their power and plumbing needs; new vs. used; service contracts. | `equipment-specialist`, `head-of-coffee`, `buildout-manager`, `procurement` | 4 |
| 21 | `coffee-sourcing-and-quality` | Evaluate roasters, run cuppings, negotiate fixed-price contracts, watch arabica prices and set recipes and dial-in. | `head-of-coffee`, `procurement`, `menu-developer`, `brand-strategist` | 4 |
| 22 | `barista-training` | Run an SCA-style curriculum covering drink standards, milk and latte art, and Cuban espresso preparation. | `head-of-coffee`, `hr-talent`, `operations-manager` | 3 |
| 23 | `sop-authoring` | Write SOPs and checklists: opening and closing, cleaning, cash handling, service and hurricane procedures. | `operations-manager`, `food-safety`, `head-of-coffee`, `cx-designer`, `hr-talent`, `risk-manager` | 6 |
| 24 | `inventory-and-procurement` | Set par levels, ordering cadence, vendor comparisons and waste tracking. | `procurement`, `operations-manager`, `menu-developer`, `data-analyst` | 4 |
| 25 | `pos-and-tech-stack` | Select and configure the POS, mobile ordering, loyalty, gift cards, delivery integrations, Wi-Fi and cameras. | `tech-architect`, `operations-manager`, `digital-marketer`, `data-analyst`, `tax-accountant` | 5 |
| 26 | `kpi-dashboard-and-alerts` | Track transactions, ticket, attach rate, labor %, COGS %, cash runway and ratings, with the early-warning triggers from 08-risks. | `data-analyst`, `engagement-lead`, `financial-modeler`, `operations-manager`, `workforce-planner`, `risk-manager`, `digital-marketer` | 7 |
| 27 | `service-design` | Design the customer journey, the ventanita-plus-café flow, queue times, layout and hospitality standards. | `cx-designer`, `concept-designer`, `operations-manager`, `buildout-manager` | 4 |
| 28 | `hiring-and-onboarding` | Write job posts and interview guides, onboard new staff and run retention programs. | `hr-talent`, `operations-manager`, `employment-counsel` | 3 |
| 29 | `brand-identity` | Develop the name, brand story, voice, visual brief and positioning statement. | `brand-strategist`, `concept-designer`, `digital-marketer`, `cultural-advisor` | 4 |
| 30 | `social-content-and-reviews` | Plan the content calendar, reels and creator work; manage the Google Business Profile and review replies. | `digital-marketer`, `brand-strategist`, `community-partnerships`, `cx-designer` | 4 |
| 31 | `launch-and-events-planning` | Run the 8-week launch plan, soft opening, PR and the Miami event calendar (Art Basel, Music Week, season). | `community-partnerships`, `brand-strategist`, `digital-marketer`, `operations-manager`, `engagement-lead` | 5 |
| 32 | `b2b-sales` | Sell office catering, coffee boxes, wholesale and retail beans, and partnerships. | `community-partnerships`, `menu-developer`, `financial-modeler` | 3 |
| 33 | `risk-register` | Maintain the ranked likelihood x impact register with owners and mitigations. | `risk-manager`, `engagement-lead`, `red-team-reviewer`, `financial-modeler` | 4 |
| 34 | `insurance-analysis` | Compare GL, BOP, property and wind, flood, business-interruption and equipment-breakdown cover and deductibles. | `risk-manager`, `site-selection`, `financial-modeler`, `corporate-counsel` | 4 |
| 35 | `hurricane-continuity` | Run the hurricane plan: NOAA monitoring, shutters, generator or backup ice, cloud POS, and reopening. | `risk-manager`, `operations-manager`, `tech-architect`, `buildout-manager` | 4 |
| 36 | `assumption-stress-test` | Challenge estimates, run downside scenarios and check claims against primary sources. | `red-team-reviewer`, `engagement-lead`, `financial-modeler`, `risk-manager` | 4 |
| 37 | `synthesis-and-decision-memos` | Combine expert outputs into client-ready recommendations and a decision log. | `engagement-lead`, `market-strategist`, `financial-modeler`, `red-team-reviewer` | 4 |
| 38 | `multi-agent-coordination` | Route questions, assign tasks, resolve conflicting advice and track open items across agents. | `engagement-lead` | 1 |

## 3. Skills by agent (reverse index)

Use this when writing each agent's definition. It is the full list of skills to give that agent.

| Agent | `agent-id` | Skills |
|---|---|---|
| Engagement Lead (orchestrator) | `engagement-lead` | `docs-knowledge-base`, `concept-positioning`, `financial-modeling`, `funding-packaging`, `kpi-dashboard-and-alerts`, `launch-and-events-planning`, `risk-register`, `assumption-stress-test`, `synthesis-and-decision-memos`, `multi-agent-coordination` |
| Red Team Reviewer | `red-team-reviewer` | `docs-knowledge-base`, `cited-web-research`, `financial-modeling`, `risk-register`, `assumption-stress-test`, `synthesis-and-decision-memos` |
| Market & Strategy Analyst | `market-strategist` | `docs-knowledge-base`, `cited-web-research`, `miami-market-data`, `concept-positioning`, `synthesis-and-decision-memos` |
| Customer Insights Researcher | `customer-insights` | `docs-knowledge-base`, `cited-web-research`, `miami-market-data`, `customer-research` |
| Competitive Intelligence Analyst | `competitive-intel` | `docs-knowledge-base`, `cited-web-research`, `competitor-mapping`, `site-scorecard` |
| Concept & Format Strategist | `concept-designer` | `docs-knowledge-base`, `competitor-mapping`, `concept-positioning`, `menu-costing-and-pricing`, `service-design`, `brand-identity` |
| Miami Culture & Localization Advisor | `cultural-advisor` | `docs-knowledge-base`, `cited-web-research`, `customer-research`, `bilingual-localization`, `brand-identity` |
| Specialty Coffee Director | `head-of-coffee` | `docs-knowledge-base`, `cited-web-research`, `menu-costing-and-pricing`, `contract-review`, `equipment-specification`, `coffee-sourcing-and-quality`, `barista-training`, `sop-authoring` |
| Menu & Food Program Developer | `menu-developer` | `docs-knowledge-base`, `competitor-mapping`, `bilingual-localization`, `menu-costing-and-pricing`, `food-safety-compliance`, `coffee-sourcing-and-quality`, `inventory-and-procurement`, `b2b-sales` |
| Site Selection & Real Estate Advisor | `site-selection` | `docs-knowledge-base`, `cited-web-research`, `miami-market-data`, `competitor-mapping`, `customer-research`, `site-scorecard`, `lease-analysis`, `permit-pathway`, `insurance-analysis` |
| Design & Buildout Project Manager | `buildout-manager` | `docs-knowledge-base`, `permit-pathway`, `contract-review`, `buildout-project-management`, `equipment-specification`, `service-design`, `hurricane-continuity` |
| Coffee Equipment & Water Specialist | `equipment-specialist` | `docs-knowledge-base`, `cited-web-research`, `contract-review`, `buildout-project-management`, `equipment-specification` |
| Technology & POS Architect | `tech-architect` | `docs-knowledge-base`, `cited-web-research`, `florida-tax-compliance`, `contract-review`, `pos-and-tech-stack`, `hurricane-continuity` |
| Data & Performance Analyst | `data-analyst` | `docs-knowledge-base`, `miami-market-data`, `financial-modeling`, `labor-modeling-and-scheduling`, `inventory-and-procurement`, `pos-and-tech-stack`, `kpi-dashboard-and-alerts` |
| Operations Manager | `operations-manager` | `docs-knowledge-base`, `labor-modeling-and-scheduling`, `food-safety-compliance`, `barista-training`, `sop-authoring`, `inventory-and-procurement`, `pos-and-tech-stack`, `kpi-dashboard-and-alerts`, `service-design`, `hiring-and-onboarding`, `launch-and-events-planning`, `hurricane-continuity` |
| Supply Chain & Procurement Specialist | `procurement` | `docs-knowledge-base`, `cited-web-research`, `menu-costing-and-pricing`, `contract-review`, `equipment-specification`, `coffee-sourcing-and-quality`, `inventory-and-procurement` |
| Food Safety & Health Compliance Officer | `food-safety` | `docs-knowledge-base`, `cited-web-research`, `permit-pathway`, `food-safety-compliance`, `sop-authoring` |
| Customer Experience & Hospitality Designer | `cx-designer` | `docs-knowledge-base`, `customer-research`, `bilingual-localization`, `sop-authoring`, `service-design`, `social-content-and-reviews` |
| HR, Hiring & Training Lead | `hr-talent` | `docs-knowledge-base`, `bilingual-localization`, `labor-modeling-and-scheduling`, `food-safety-compliance`, `employment-compliance-fl`, `barista-training`, `sop-authoring`, `hiring-and-onboarding` |
| Labor & Workforce Planner | `workforce-planner` | `docs-knowledge-base`, `labor-modeling-and-scheduling`, `employment-compliance-fl`, `kpi-dashboard-and-alerts` |
| Financial Planning & Analysis Lead | `financial-modeler` | `docs-knowledge-base`, `concept-positioning`, `site-scorecard`, `lease-analysis`, `financial-modeling`, `menu-costing-and-pricing`, `labor-modeling-and-scheduling`, `funding-packaging`, `florida-tax-compliance`, `buildout-project-management`, `kpi-dashboard-and-alerts`, `b2b-sales`, `risk-register`, `insurance-analysis`, `assumption-stress-test`, `synthesis-and-decision-memos` |
| Funding & Capital Advisor | `funding-advisor` | `docs-knowledge-base`, `cited-web-research`, `financial-modeling`, `funding-packaging` |
| Accounting & Tax Advisor | `tax-accountant` | `docs-knowledge-base`, `cited-web-research`, `florida-tax-compliance`, `employment-compliance-fl`, `pos-and-tech-stack` |
| Business Formation & Contracts Counsel | `corporate-counsel` | `docs-knowledge-base`, `cited-web-research`, `funding-packaging`, `contract-review`, `insurance-analysis` |
| Commercial Lease Counsel | `lease-counsel` | `docs-knowledge-base`, `cited-web-research`, `lease-analysis`, `permit-pathway`, `contract-review` |
| Permits & Licensing Expeditor | `permits-expeditor` | `docs-knowledge-base`, `cited-web-research`, `site-scorecard`, `florida-tax-compliance`, `permit-pathway`, `buildout-project-management` |
| Employment Law Advisor | `employment-counsel` | `docs-knowledge-base`, `cited-web-research`, `employment-compliance-fl`, `hiring-and-onboarding` |
| Brand & Marketing Strategist | `brand-strategist` | `docs-knowledge-base`, `cited-web-research`, `competitor-mapping`, `customer-research`, `bilingual-localization`, `concept-positioning`, `coffee-sourcing-and-quality`, `brand-identity`, `social-content-and-reviews`, `launch-and-events-planning` |
| Digital, Social & Reputation Marketer | `digital-marketer` | `docs-knowledge-base`, `bilingual-localization`, `pos-and-tech-stack`, `kpi-dashboard-and-alerts`, `brand-identity`, `social-content-and-reviews`, `launch-and-events-planning` |
| Community, PR & B2B Partnerships Manager | `community-partnerships` | `docs-knowledge-base`, `cited-web-research`, `bilingual-localization`, `social-content-and-reviews`, `launch-and-events-planning`, `b2b-sales` |
| Risk, Insurance & Business Continuity Advisor | `risk-manager` | `docs-knowledge-base`, `cited-web-research`, `site-scorecard`, `lease-analysis`, `sop-authoring`, `kpi-dashboard-and-alerts`, `risk-register`, `insurance-analysis`, `hurricane-continuity`, `assumption-stress-test` |

## 4. Notes for building the team

- **Most shared skills (build and test these first):** `docs-knowledge-base` (31), `cited-web-research` (20), `kpi-dashboard-and-alerts` (7), `contract-review` (7), `bilingual-localization` (7), `sop-authoring` (6).
- **Suggested build order:** `engagement-lead`, then the Core agents (strategy, site, finance, permits, lease, coffee, operations, people, brand, risk), then `red-team-reviewer` to check their output, then the On-demand specialists.
- **Overlap is intentional.** For example, `lease-counsel` covers the legal terms of a lease while `site-selection` covers whether the location suits the business, and both use `lease-analysis`. `engagement-lead` resolves any conflicting advice.
- **Human sign-off still required.** Legal, tax, insurance and permit agents give research-grade guidance only. Licensed professionals must confirm their output before anything is signed or filed.
- **Keep the docs current.** Agents should write new findings back into `docs/` using the shared labels, so the whole team works from the same facts.
