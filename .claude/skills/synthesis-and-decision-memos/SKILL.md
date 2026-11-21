---
name: synthesis-and-decision-memos
description: "Combine several experts' outputs into one client-ready recommendation or decision memo, resolve or surface disagreements, and record decisions in docs/decision-log.md."
when_to_use: "Use when several expert answers must become one answer, a decision memo, an executive summary or a decision-log entry."
---

# Synthesis and decision memos

## Combine
1. Lead with the answer and recommendation in 1–3 sentences.
2. Merge overlapping points; keep the strongest evidence for each.
3. Where experts disagree: state each position, the evidence, and your resolution (or say it needs the client's call and why).
4. Keep labels (Fact/Estimate/Assumption/To verify) and sources from the experts.
5. Attribute key points to the expert role that made them.

## Decision memo format
```
# Decision: <title>            Date:            Status: proposed / decided
Question:
Recommendation:
Options considered: (pros, cons, cost, risk for each)
Evidence: (labelled, sourced)
Risks and mitigations:
Red-team verdict:
Open items / to verify:
Next steps, owners, dates:
```

## Decision log
When the client decides, add an entry to `docs/decision-log.md`: date, decision, options, chosen option, rationale, owner, links. Never rewrite past entries; add a new entry that supersedes them.
