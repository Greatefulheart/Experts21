# Expert Roster: Advisory Agent Team

This is the expert team a consultant would want around them for the **Miami specialty coffee shop** project. It is built from the research in this folder ([README](README.md)). Every role is a Claude Code project subagent in `.claude/agents/<agent-id>.md`, and every skill is a project skill in `.claude/skills/<skill-id>/SKILL.md`. Skills are shared, so several agents can use the same skill. See [`CLAUDE.md`](../CLAUDE.md) for how to use the team.

- **33 agents** (31 experts in 11 domains, plus the `orchestrator` and the `meta-agent`) and **39 shared skills**.
- **Tier:** *Core* experts take part in most decisions. *On-demand* experts are called in for specialist questions. The *Entry point* is where questions start. *Maintenance* builds and improves the team.
- **Key docs** are the research files each agent loads as context (01 = `01-market.md`, and so on).

## 1. Agents


### Team infrastructure

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 1 | **Orchestrator** | `orchestrator` | Entry point | Takes any question about the project, decides which experts to bring in, has them work together, and returns one combined answer. | All |
| 2 | **Meta Agent (team builder)** | `meta-agent` | Maintenance | Creates new expert agents and skills, improves existing ones, and keeps the team definitions, roster and docs consistent. | expert-roster, CLAUDE.md, .claude/ |

### Leadership

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 3 | **Engagement Lead** | `engagement-lead` | Core | Owns the engagement plan, decision log and client deliverables, and turns the experts' advice into client-ready recommendations. | All |
| 4 | **Red Team Reviewer** | `red-team-reviewer` | Core | Challenges every major recommendation by testing assumptions, running downside cases and checking sources before advice reaches the client. | All, esp. 04, 08 |

### Business & strategy

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 5 | **Market & Strategy Analyst** | `market-strategist` | Core | Sizes the Miami specialty-coffee opportunity and turns market trends into a go/no-go case and a growth strategy. | 01, 02, 03 |
| 6 | **Customer Insights Researcher** | `customer-insights` | On-demand | Defines and validates the customer segments with demographics, bilingual surveys and foot-traffic counts. | 02 |
| 7 | **Competitive Intelligence Analyst** | `competitive-intel` | Core | Maps and monitors specialty roasters, ventanitas and chains around each candidate site, including their prices, formats and gaps. | 03 |
| 8 | **Concept & Format Strategist** | `concept-designer` | Core | Chooses the shop format and positioning (Cuban x specialty, cowork café, or grab-and-go) and sets the seat count and service model. | 02, 03, 07 |
| 9 | **Miami Culture & Localization Advisor** | `cultural-advisor` | On-demand | Makes sure the concept, menu, language and service fit Miami's bilingual, Cuban-rooted coffee culture. | 02, 03, 07 |

### Coffee & product

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 10 | **Specialty Coffee Director** | `head-of-coffee` | Core | Picks the roaster partner, sets recipes and quality standards, manages green-coffee price exposure, and leads barista craft. | 01, 03, 04, 08 |
| 11 | **Menu & Food Program Developer** | `menu-developer` | On-demand | Designs the drink and food menu and the price ladder ($3 Cuban espresso up to premium) while hitting COGS targets. | 03, 04 |

### Real estate & build

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 12 | **Site Selection & Real Estate Advisor** | `site-selection` | Core | Finds and scores candidate locations on traffic, rent plus NNN, parking, flood zone, zoning and competitor density. | 02, 03, 04, 08 |
| 13 | **Design & Buildout Project Manager** | `buildout-manager` | On-demand | Manages the architect, contractor and inspections so the space opens on schedule and within the buildout budget. | 04, 05, 08 |

### Technical

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 14 | **Coffee Equipment & Water Specialist** | `equipment-specialist` | On-demand | Specifies the espresso machine, grinders, water filtration and refrigeration, plus the power and plumbing they need and their service contracts. | 04, 08 |
| 15 | **Technology & POS Architect** | `tech-architect` | On-demand | Selects and integrates the POS, mobile ordering, loyalty, delivery, Wi-Fi and security systems. | 04, 07 |
| 16 | **Data & Performance Analyst** | `data-analyst` | On-demand | Builds the KPI dashboard and early-warning alerts (transactions, ticket, labor %, COGS %, cash runway, ratings). | 04, 08 |

### Operations

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 17 | **Operations Manager** | `operations-manager` | Core | Designs daily operations: SOPs, opening and closing, quality control, vendor flow and shift management. | 04, 06, 08 |
| 18 | **Supply Chain & Procurement Specialist** | `procurement` | On-demand | Sources and contracts coffee, milk, food, packaging and smallwares at the best total cost, and manages par levels. | 01, 04, 08 |
| 19 | **Food Safety & Health Compliance Officer** | `food-safety` | On-demand | Keeps the shop inspection-ready: DBPR standards, food-manager certification, staff food-safety training and logs. | 05, 06 |
| 20 | **Customer Experience & Hospitality Designer** | `cx-designer` | On-demand | Designs the customer journey (ventanita window, counter and seating), queue flow and hospitality standards. | 02, 07 |

### People

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 21 | **HR, Hiring & Training Lead** | `hr-talent` | Core | Hires, onboards, trains and keeps a bilingual team, with pay and culture that reduce barista turnover. | 06 |
| 22 | **Labor & Workforce Planner** | `workforce-planner` | On-demand | Models staffing and schedules against sales so labor stays at 28–35% of revenue under Florida's $15 minimum wage. | 04, 06 |

### Finance

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 23 | **Financial Planning & Analysis Lead** | `financial-modeler` | Core | Owns the startup budget, monthly P&L, 36-month cash-flow model, break-even and scenarios. | 04, 06, 08 |
| 24 | **Funding & Capital Advisor** | `funding-advisor` | On-demand | Structures the funding mix (savings, SBA 7(a) or microloan, equipment financing, investors) and prepares lender packages. | 04, 08 |
| 25 | **Accounting & Tax Advisor** | `tax-accountant` | On-demand | Sets up bookkeeping and payroll, and handles Florida sales tax (7% in Miami-Dade), reemployment tax and local tax receipts. | 04, 05, 06 |

### Legal

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 26 | **Business Formation & Contracts Counsel** | `corporate-counsel` | On-demand | Forms the entity and reviews supplier, contractor, equipment and partner contracts. | 05 |
| 27 | **Commercial Lease Counsel** | `lease-counsel` | Core | Negotiates and reviews the lease: NNN/CAM, TI allowance, free rent, permit contingency, personal guarantee and term. | 04, 05, 08 |
| 28 | **Permits & Licensing Expeditor** | `permits-expeditor` | Core | Identifies the jurisdiction and drives every permit to approval: zoning, CU, BTR, DBPR, DERM, sidewalk café and signage. | 05 |
| 29 | **Employment Law Advisor** | `employment-counsel` | On-demand | Keeps hiring and pay compliant: minimum and tipped wage, tip pools, E-Verify, workers' comp and required posters. | 06 |

### Marketing

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 30 | **Brand & Marketing Strategist** | `brand-strategist` | Core | Defines the brand, positioning and marketing plan and budget, tied to the target segments. | 02, 03, 07 |
| 31 | **Digital, Social & Reputation Marketer** | `digital-marketer` | On-demand | Runs bilingual Instagram and TikTok, the Google Business Profile, reviews, email/SMS and app-based loyalty campaigns. | 07 |
| 32 | **Community, PR & B2B Partnerships Manager** | `community-partnerships` | On-demand | Builds press, creator, event (Art Basel and others) and office/catering and wholesale partnerships. | 07 |

### Risk

| # | Agent | `agent-id` | Tier | Job description (one line) | Key docs |
|---|---|---|---|---|---|
| 33 | **Risk, Insurance & Business Continuity Advisor** | `risk-manager` | Core | Maintains the risk register, insurance program and hurricane plan, and watches the early-warning indicators. | 08, 04 |

## 2. Shared skills and the agents that use them

| # | `skill-id` | What the skill does | Used by | # agents |
|---|---|---|---|---|
| 1 | `docs-knowledge-base` | Read and update the project's research pack in docs/ and answer in the team's standard expert format, using the Fact / Estimate / Assumption / To-verify labels. | **All agents** | 33 |
| 2 | `cited-web-research` | Find current public information on the web and cite every fact with a link and a date; prefer primary sources and flag stale or second-hand ones. | `market-strategist`, `customer-insights`, `competitive-intel`, `cultural-advisor`, `head-of-coffee`, `site-selection`, `equipment-specialist`, `tech-architect`, `procurement`, `food-safety`, `funding-advisor`, `tax-accountant`, `corporate-counsel`, `lease-counsel`, `permits-expeditor`, `employment-counsel`, `brand-strategist`, `community-partnerships`, `risk-manager`, `red-team-reviewer` | 20 |
| 3 | `miami-market-data` | Pull and interpret Miami-Dade demographic, establishment and visitor data (Census/ACS, County Business Patterns NAICS 722515, GMCVB) at county and neighborhood level. | `market-strategist`, `customer-insights`, `site-selection`, `data-analyst` | 4 |
| 4 | `competitor-mapping` | Map every coffee seller within a set radius of a site and run a structured mystery-shop checklist (prices, ticket, queue, seats, busy hours, ratings). | `competitive-intel`, `site-selection`, `concept-designer`, `menu-developer`, `brand-strategist` | 5 |
| 5 | `customer-research` | Design bilingual surveys, intercept interviews and foot-traffic counts, and turn the results into segment personas and willingness-to-pay estimates. | `customer-insights`, `site-selection`, `cx-designer`, `brand-strategist`, `cultural-advisor` | 5 |
| 6 | `bilingual-localization` | Write and review English/Spanish copy for Miami, use Cuban coffee terms correctly, and check the cultural fit of names, menus, signs and campaigns. | `cultural-advisor`, `brand-strategist`, `digital-marketer`, `menu-developer`, `cx-designer`, `hr-talent`, `community-partnerships` | 7 |
| 7 | `concept-positioning` | Score shop format and positioning options (kiosk, café, roastery-café; Cuban x specialty, cowork café, grab-and-go) against market fit, cost, operations and risk. | `concept-designer`, `market-strategist`, `brand-strategist`, `financial-modeler`, `engagement-lead` | 5 |
| 8 | `site-scorecard` | Score candidate sites on foot traffic, rent plus NNN, parking, FEMA flood zone, zoning, visibility, competitor density and buildout condition. | `site-selection`, `competitive-intel`, `permits-expeditor`, `risk-manager`, `financial-modeler` | 5 |
| 9 | `lease-analysis` | Analyze commercial lease terms: base rent, NNN/CAM, escalations, TI allowance, free rent, permit contingency, use and exclusivity clauses, guarantee, term and occupancy cost as a share of revenue. | `lease-counsel`, `site-selection`, `financial-modeler`, `risk-manager` | 4 |
| 10 | `financial-modeling` | Build and check the startup budget, monthly P&L, 36-month cash flow, break-even and base/downside/upside scenarios for the coffee shop. | `financial-modeler`, `funding-advisor`, `data-analyst`, `red-team-reviewer`, `engagement-lead` | 5 |
| 11 | `menu-costing-and-pricing` | Cost each menu item from its recipe, build the price ladder, keep beverage COGS at 15–20% and total COGS at 25–35%, and model price changes. | `menu-developer`, `head-of-coffee`, `procurement`, `financial-modeler`, `concept-designer` | 5 |
| 12 | `labor-modeling-and-scheduling` | Model staffing coverage by hour and its cost under Florida wage law, hit the 28–35% labor target, and build schedules from POS sales data. | `workforce-planner`, `hr-talent`, `operations-manager`, `financial-modeler`, `data-analyst` | 5 |
| 13 | `funding-packaging` | Prepare funding options and lender or investor packages: SBA 7(a) and microloans, equipment financing, investor terms, use of funds and repayment from the cash-flow model. | `funding-advisor`, `financial-modeler`, `corporate-counsel`, `engagement-lead` | 4 |
| 14 | `florida-tax-compliance` | Apply Florida and Miami-Dade business taxes: 7% sales tax (6% state + 1% county surtax), DR-15 filing, reemployment tax, local food-and-beverage or resort taxes, business tax receipts, and POS tax setup. | `tax-accountant`, `permits-expeditor`, `financial-modeler`, `tech-architect` | 4 |
| 15 | `permit-pathway` | Identify which jurisdiction governs a Miami-area address and list, sequence and track every required permit: zoning, Certificate of Use, city and county BTR, DBPR food license and plan review, DERM/WASD, building, sidewalk café and signs. | `permits-expeditor`, `buildout-manager`, `site-selection`, `food-safety`, `lease-counsel` | 5 |
| 16 | `food-safety-compliance` | Apply Florida DBPR food-service standards: certified food manager rules, staff food-safety training, inspection readiness, temperature and cleaning logs, and allergen handling for a coffee shop. | `food-safety`, `operations-manager`, `hr-talent`, `menu-developer` | 4 |
| 17 | `employment-compliance-fl` | Apply Florida and federal employment rules for a coffee shop: $15 minimum wage, $11.98 tipped cash wage and tip-credit conditions, tip pools, E-Verify for 25+ employees, I-9, workers' comp, minors and required posters. | `employment-counsel`, `hr-talent`, `workforce-planner`, `tax-accountant` | 4 |
| 18 | `contract-review` | Review supplier, roaster, equipment-lease, contractor, software and partnership contracts, summarize key terms and flag risky clauses with suggested fixes. | `corporate-counsel`, `lease-counsel`, `procurement`, `head-of-coffee`, `equipment-specialist`, `buildout-manager`, `tech-architect` | 7 |
| 19 | `buildout-project-management` | Plan and track the café buildout: scope, schedule, budget with contingency, bids, change orders, inspections and the 10–30% overrun risk. | `buildout-manager`, `permits-expeditor`, `equipment-specialist`, `financial-modeler` | 4 |
| 20 | `equipment-specification` | Specify espresso machines, grinders, brewers, water filtration, refrigeration and ice machines sized to forecast volume, with utility requirements, new vs. used vs. lease comparison and service contracts. | `equipment-specialist`, `head-of-coffee`, `buildout-manager`, `procurement` | 4 |
| 21 | `coffee-sourcing-and-quality` | Evaluate roasters, run cuppings, negotiate supply contracts with price protection, watch arabica prices, and set recipes and dial-in standards for espresso, Cuban espresso, filter and cold brew. | `head-of-coffee`, `procurement`, `menu-developer`, `brand-strategist` | 4 |
| 22 | `barista-training` | Run a barista training program: SCA-style fundamentals, espresso and milk standards, latte art, Cuban espresso preparation, workflow at peak, cleaning and hospitality. | `head-of-coffee`, `hr-talent`, `operations-manager` | 3 |
| 23 | `sop-authoring` | Write clear standard operating procedures and checklists: opening, closing, cleaning, cash handling, service, deliveries, equipment failure and hurricane procedures. | `operations-manager`, `food-safety`, `head-of-coffee`, `cx-designer`, `hr-talent`, `risk-manager` | 6 |
| 24 | `inventory-and-procurement` | Set par levels and order cadence, compare vendors on total landed cost, track waste, and plan supply for hurricane season. | `procurement`, `operations-manager`, `menu-developer`, `data-analyst` | 4 |
| 25 | `pos-and-tech-stack` | Select and configure the shop's technology: POS, payments, mobile ordering, loyalty and gift cards, delivery integrations, Wi-Fi, cameras and music, with total cost and data flows. | `tech-architect`, `operations-manager`, `digital-marketer`, `data-analyst`, `tax-accountant` | 5 |
| 26 | `kpi-dashboard-and-alerts` | Define and track the shop's KPIs (transactions, ticket, attach rate, labor %, COGS %, occupancy %, cash runway, ratings, app share) with targets and early-warning alerts from the risk register. | `data-analyst`, `engagement-lead`, `financial-modeler`, `operations-manager`, `workforce-planner`, `risk-manager`, `digital-marketer` | 7 |
| 27 | `service-design` | Design the customer journey and service flow: ventanita plus café, queue and pickup flow for walk-ins and mobile orders, seating and laptop policy, hospitality standards and service recovery. | `cx-designer`, `concept-designer`, `operations-manager`, `buildout-manager` | 4 |
| 28 | `hiring-and-onboarding` | Write bilingual job posts and interview guides, run hiring, onboard new staff and run retention programs to reduce barista turnover. | `hr-talent`, `operations-manager`, `employment-counsel` | 3 |
| 29 | `brand-identity` | Develop the brand: name, positioning statement, story, voice, visual direction brief and naming checks for the Miami coffee shop. | `brand-strategist`, `concept-designer`, `digital-marketer`, `cultural-advisor` | 4 |
| 30 | `social-content-and-reviews` | Plan and run bilingual social content (Instagram, TikTok), the Google Business Profile, creator collaborations, and the review program including replies. | `digital-marketer`, `brand-strategist`, `community-partnerships`, `cx-designer` | 4 |
| 31 | `launch-and-events-planning` | Run the 8-week launch plan and the Miami event calendar: soft opening, grand opening, press and creator invites, Art Basel, Miami Music Week, F1, National Coffee Day and seasonal pushes. | `community-partnerships`, `brand-strategist`, `digital-marketer`, `operations-manager`, `engagement-lead` | 5 |
| 32 | `b2b-sales` | Sell and run B2B revenue: office catering and coffee boxes, building and coworking partnerships, wholesale and retail beans, with pricing and margin checks. | `community-partnerships`, `menu-developer`, `financial-modeler` | 3 |
| 33 | `risk-register` | Maintain the ranked risk register (likelihood x impact) with owners, mitigations, triggers and review dates, starting from docs/08-risks.md. | `risk-manager`, `engagement-lead`, `red-team-reviewer`, `financial-modeler` | 4 |
| 34 | `insurance-analysis` | Compare insurance cover for a Miami coffee shop: general liability, BOP, property including wind, flood, business interruption, equipment breakdown, workers' comp, liquor if relevant; deductibles and site flood zone. | `risk-manager`, `site-selection`, `financial-modeler`, `corporate-counsel` | 4 |
| 35 | `hurricane-continuity` | Run the hurricane and business-continuity plan: NOAA monitoring, watch/warning checklists, shutters and equipment protection, backup power and ice, cloud POS, staff communication, and reopening. | `risk-manager`, `operations-manager`, `tech-architect`, `buildout-manager` | 4 |
| 36 | `assumption-stress-test` | Challenge estimates and recommendations: find the critical assumptions, recompute numbers, run downside scenarios and check claims against primary sources. | `red-team-reviewer`, `engagement-lead`, `financial-modeler`, `risk-manager` | 4 |
| 37 | `synthesis-and-decision-memos` | Combine several experts' outputs into one client-ready recommendation or decision memo, resolve or surface disagreements, and record decisions in docs/decision-log.md. | `orchestrator`, `engagement-lead`, `market-strategist`, `financial-modeler`, `red-team-reviewer` | 5 |
| 38 | `multi-agent-coordination` | Route a question to the right expert agents, brief them, run them in parallel or in sequence, run cross-review when they disagree, and track open items. Includes the team's routing map. | `orchestrator` | 1 |
| 39 | `team-authoring` | Create, change and validate this project's Claude Code subagents and skills: file formats, frontmatter fields, naming, wiring agents to skills, roster and routing-map upkeep, and the validator script. | `meta-agent` | 1 |

## 3. Skills by agent (reverse index)

This matches the `skills:` list in each agent file.

| Agent | `agent-id` | Skills |
|---|---|---|
| Orchestrator | `orchestrator` | `docs-knowledge-base`, `synthesis-and-decision-memos`, `multi-agent-coordination` |
| Meta Agent (team builder) | `meta-agent` | `docs-knowledge-base`, `team-authoring` |
| Engagement Lead | `engagement-lead` | `docs-knowledge-base`, `concept-positioning`, `financial-modeling`, `funding-packaging`, `kpi-dashboard-and-alerts`, `launch-and-events-planning`, `risk-register`, `assumption-stress-test`, `synthesis-and-decision-memos` |
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

## 4. Notes

- **Most shared skills:** `docs-knowledge-base` (33), `cited-web-research` (20), `kpi-dashboard-and-alerts` (7), `contract-review` (7), `bilingual-localization` (7), `sop-authoring` (6).
- **Who delegates:** only the `orchestrator` starts other agents. Experts name the colleague who should handle a hand-off, and the orchestrator routes it.
- **Who edits `docs/`:** `orchestrator`, `engagement-lead` and `meta-agent`. Other experts propose changes in their answers.
- **Overlap is intentional.** For example, `lease-counsel` covers the legal terms of a lease while `site-selection` covers whether the location suits the business, and both use `lease-analysis`. The orchestrator resolves conflicting advice, and `engagement-lead` records decisions.
- **Human sign-off still required.** Legal, tax, insurance and permit agents give research-grade guidance only. Licensed professionals must confirm their output before anything is signed or filed.
- **Changing the team:** ask `meta-agent`. It keeps the agent files, skills, this roster and `CLAUDE.md` in sync and runs `.claude/skills/team-authoring/scripts/validate_team.py`.
