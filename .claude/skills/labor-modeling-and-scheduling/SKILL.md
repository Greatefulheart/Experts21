---
name: labor-modeling-and-scheduling
description: "Model staffing coverage by hour and its cost under Florida wage law, hit the 28–35% labor target, and build schedules from POS sales data."
when_to_use: "Use for staffing levels, labor budgets, opening hours, schedules or labor-percentage problems."
---

# Labor modeling and scheduling

## Inputs (docs/06)
- Florida minimum wage $15.00/hr from Sept 30, 2026; tipped cash wage $11.98 (tip credit $3.02). Expected inflation indexing from Sept 30, 2027 (To verify).
- Base model: 7am–6pm, 7 days (77 hrs/week); 2 baristas at all times, 3rd at 7–11am and weekends, ~190 barista hours/week; blended $16.50/hr, ~$13.6K/month; manager ~$5.4K/month; +~10% payroll taxes and workers' comp; total ~$19K–$21.5K/month.
- Target labor 28–35% of revenue, which needs ~$60K+/month revenue on this model.

## Method
1. Forecast transactions by hour (from POS once open; from counts and benchmarks before).
2. Convert to staff needed by hour (e.g., one barista per ~30–40 drinks/hour at peak, Assumption to validate).
3. Respect a certified food manager on shift when 3+ food employees work.
4. Cost the schedule; compare to labor % target; adjust hours, shift lengths and stations.
5. After opening: weekly review of labor % and sales per labor hour.

## Levers
Shorter hours (close at 3pm), split shifts, cross-training, mobile-order batching, fewer menu items at peak.
