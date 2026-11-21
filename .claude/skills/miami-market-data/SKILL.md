---
name: miami-market-data
description: "Pull and interpret Miami-Dade demographic, establishment and visitor data (Census/ACS, County Business Patterns NAICS 722515, GMCVB) at county and neighborhood level."
when_to_use: "Use for population, income, age, Hispanic share, worker and visitor counts, coffee-shop density per capita, or any neighborhood-level demand sizing in Miami."
---

# Miami market data

## Baseline (from docs/01 and docs/02)
- Miami-Dade population ~2.80M (2025), 70.6% Hispanic or Latino.
- Median household income $77,859 (2025 ACS) / $71,753 (2020–24 5-year ACS).
- ~20.1M overnight visitors a year (GMCVB, 2024).
- WalletHub (via secondary source): Miami 4th for coffee lovers, 12th for shops per capita (2025). To verify.

## Sources and what to pull
| Need | Source | Notes |
|---|---|---|
| Population, age, income by tract or ZIP | data.census.gov (ACS 5-year) | Use 5-year for small areas |
| Coffee shop counts | Census County Business Patterns, NAICS 722515 | County and ZIP level |
| Workers near a site | Census OnTheMap (LEHD) | Daytime population matters for Brickell/Downtown |
| Visitors | GMCVB research and statistics | Season, neighborhood of stay |
| Wages | BLS OEWS, Miami-Fort Lauderdale-West Palm Beach MSA | For labor costs |

## Trade-area sizing method
1. Define the trade area (walk: 0.25–0.5 mile; drive: 5–10 minutes).
2. Count residents, daytime workers and visitor rooms in it.
3. Apply participation rates (Assumption until surveyed): share who buy coffee away from home weekly, visits per week, share capturable by us.
4. Compare with the number of competing outlets to get demand per outlet.
5. Present a low/base/high range and label it an Estimate.
