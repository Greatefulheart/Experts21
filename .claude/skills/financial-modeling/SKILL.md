---
name: financial-modeling
description: "Build and check the startup budget, monthly P&L, 36-month cash flow, break-even and base/downside/upside scenarios for the coffee shop."
when_to_use: "Use for any question about costs, revenue, profit, cash needs, break-even, payback, ROI or whether the numbers work."
---

# Financial modeling

## Starting point (docs/04)
- Startup: low ~$150K / mid ~$315K / high ~$585K for a 1,000–1,400 sq ft café (Estimate).
- Benchmarks: COGS 25–35% (beverage 15–20%), labor 28–35%, card fees ~3%, net margin 2.5–7%.
- Example P&L: ~$45K/month revenue roughly breaks even; ~$65K/month gives ~$10.95K operating profit before debt and owner pay. Break-even ~190–210 transactions/day at a $7.50 ticket (Estimate).

## Model structure
1. **Inputs sheet**: every assumption in one place, labelled Fact/Estimate/Assumption with source.
2. **Revenue**: transactions/day by daypart x average ticket x days open; ramp-up curve (e.g., 50% of steady state in month 1 rising to 100% by month 6–9, Assumption); seasonality (Nov–Apr higher, Jun–Sep lower).
3. **Costs**: COGS %, labor from the labor model, occupancy, utilities, card fees, insurance, marketing, software, repairs, licenses, accounting.
4. **Cash flow**: startup spend timing, working capital, debt service, owner draw, taxes.
5. **Outputs**: monthly P&L, cumulative cash, minimum cash point, break-even month, payback, break-even transactions per day.

## Scenarios
Base, downside (traffic -20%, opening 2 months late, buildout +20%, labor +5%) and upside. Report the minimum cash balance in each.

## Rules
- Do arithmetic with Bash/Python, never in your head; show formulas.
- Keep units consistent (monthly vs. annual; $/sq ft/yr).
- Every output table states its assumptions and date.
