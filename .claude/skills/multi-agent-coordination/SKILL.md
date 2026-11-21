---
name: multi-agent-coordination
description: "Route a question to the right expert agents, brief them, run them in parallel or in sequence, run cross-review when they disagree, and track open items. Includes the team's routing map."
when_to_use: "Use when acting as the orchestrator: deciding which experts to involve in a question and coordinating their work."
---

# Multi-agent coordination

## Routing map (topic → experts)
| Topic | Lead expert | Usually add |
|---|---|---|
| Go/no-go, overall strategy | market-strategist | financial-modeler, competitive-intel, red-team-reviewer |
| Customers, segments, demand | customer-insights | market-strategist, cultural-advisor |
| Competitors, pricing vs. market | competitive-intel | menu-developer, site-selection |
| Concept, format, positioning | concept-designer | brand-strategist, financial-modeler, cx-designer |
| Location, neighborhood, listing | site-selection | competitive-intel, permits-expeditor, risk-manager |
| Lease, LOI | lease-counsel | site-selection, financial-modeler, red-team-reviewer |
| Budget, P&L, break-even, cash | financial-modeler | red-team-reviewer, + topic owner |
| Funding, loans, investors | funding-advisor | financial-modeler, corporate-counsel, red-team-reviewer |
| Taxes, bookkeeping | tax-accountant | financial-modeler |
| Permits, zoning, licenses | permits-expeditor | buildout-manager, food-safety |
| Buildout, construction | buildout-manager | equipment-specialist, permits-expeditor, financial-modeler |
| Equipment | equipment-specialist | head-of-coffee, buildout-manager |
| Coffee, roaster, quality | head-of-coffee | procurement, menu-developer |
| Menu, prices, COGS | menu-developer | head-of-coffee, financial-modeler, competitive-intel |
| Suppliers, inventory | procurement | head-of-coffee, operations-manager |
| Operations, SOPs | operations-manager | food-safety, workforce-planner, cx-designer |
| Food safety | food-safety | operations-manager |
| Customer experience, layout | cx-designer | operations-manager, buildout-manager |
| Hiring, training, culture | hr-talent | employment-counsel, head-of-coffee |
| Staffing levels, labor cost | workforce-planner | financial-modeler, employment-counsel |
| Employment law | employment-counsel | hr-talent |
| Entity, contracts | corporate-counsel | tax-accountant |
| Brand, marketing plan | brand-strategist | cultural-advisor, digital-marketer |
| Social, reviews, loyalty | digital-marketer | tech-architect, brand-strategist |
| PR, events, B2B | community-partnerships | brand-strategist, menu-developer |
| POS, tech | tech-architect | operations-manager, data-analyst |
| KPIs, performance | data-analyst | financial-modeler, operations-manager |
| Risks, insurance, hurricanes | risk-manager | financial-modeler, operations-manager |
| Plans, memos, decision log | engagement-lead | (whoever produced the inputs) |
| Language and culture | cultural-advisor | brand-strategist |

## Procedure
1. **Classify**: restate the question, list sub-questions, pick the lead and supporting experts (usually 2–6; one is fine for a narrow question).
2. **Brief** each expert in a self-contained prompt (they do not see this conversation): the client question, their sub-question, relevant docs, constraints and decisions already made, what other experts are covering, and "answer in the standard expert response format".
3. **Run** independent experts in parallel; run dependent ones in sequence (e.g., site-selection before lease-counsel, menu-developer before financial-modeler).
4. **Cross-review** if answers conflict, a number differs by more than ~10%, or the decision is high-stakes: send the conflicting points to the relevant experts and/or `red-team-reviewer` with the other side's evidence.
5. **Synthesize** with `synthesis-and-decision-memos`.
6. **Close**: list open items with owners; say which experts were consulted.

## Limits
Agents nest at most 3 levels below the main conversation and up to 20 run at once; keep fan-out modest. Experts cannot spawn other agents, so you do all routing.
