---
name: assumption-stress-test
description: "Challenge estimates and recommendations: find the critical assumptions, recompute numbers, run downside scenarios and check claims against primary sources."
when_to_use: "Use before finalising any recommendation that depends on estimates, and for go/no-go, lease, funding or major-spend decisions."
---

# Assumption stress test

## Procedure
1. State the recommendation in one sentence.
2. List the assumptions it depends on; rank by impact x uncertainty; take the top 3–7.
3. For each: what evidence supports it (label), what would make it wrong, a plausible bad value.
4. Recompute key numbers independently with Bash/Python.
5. Downside case: traffic -20%, ticket -5%, opening +2 months, buildout +20%, labor +5%, rent +10% (adjust to the question). Does the recommendation still hold? What is the minimum cash point?
6. Check sources: primary? dated? second-hand? vendor-biased?
7. Verdict: holds / holds with conditions / does not hold, plus the conditions or the fix.

## Output
A table: assumption, label, evidence, risk if wrong, test result. Then the verdict and the 1–3 things that would most change the answer. Be direct; do not soften real problems.
