---
name: docs-knowledge-base
description: "Read and update the project's research pack in docs/ and answer in the team's standard expert format, using the Fact / Estimate / Assumption / To-verify labels."
when_to_use: "Use for any work on the Miami specialty coffee shop project: before answering, to find the relevant research; and when proposing changes to the docs."
---

# Docs knowledge base

The shared source of truth for the whole team is the `docs/` folder at the project root.

## Files
| File | Covers |
|---|---|
| `docs/README.md` | Index, headline findings, label conventions |
| `docs/01-market.md` | Market size, growth, Miami demand, coffee prices |
| `docs/02-target-customers.md` | Demographics and six customer segments |
| `docs/03-competitors.md` | Specialty roasters, ventanitas, chains, gaps |
| `docs/04-startup-and-operating-costs.md` | Startup budget, rent, monthly P&L, break-even, sales tax |
| `docs/05-permits-and-licenses.md` | Permits, licenses, taxes, sequence |
| `docs/06-staffing.md` | Wage law, roles, labor model, compliance |
| `docs/07-marketing.md` | Positioning, channels, calendar, launch |
| `docs/08-risks.md` | Ranked risks, mitigations, early-warning indicators |
| `docs/expert-roster.md` | Every agent and skill, and who uses what |
| `docs/decision-log.md` | Decisions taken, with evidence |

## Before you answer
1. Read the files listed as your key docs, plus any file the question touches. Use Grep to find specific numbers.
2. Prefer what the docs say over memory. If you have newer or better evidence, say so and cite it.
3. Check `docs/decision-log.md` so you do not contradict a decision already taken (or say clearly that you recommend revisiting it).

## Labels (use them in every answer)
- **Fact**: has a source link and, where known, a date.
- **Estimate**: a planning number built from several sources. Show how it was built.
- **Assumption**: a value chosen so a model works. Say what real data would replace it.
- **To verify**: an open question a person or agent with live access should settle.

## Standard expert response format
Return your answer in this structure so the orchestrator can merge it:

```
## <Your role>: <one-line answer>
**Recommendation:** ...
**Reasoning:** 3–6 bullets
**Key numbers / facts:** labelled Fact / Estimate / Assumption, with sources
**Risks and caveats:** ...
**Depends on / consult:** other experts whose input changes this answer
**To verify:** ...
**Proposed doc updates:** file, section, exact change (or "none")
**Confidence:** high / medium / low, and why
```

## Editing docs
Only `engagement-lead`, `orchestrator` and `meta-agent` edit files in `docs/`. Every other expert proposes changes under **Proposed doc updates**. When editing: keep the labels, add the source and date, update `Research date` lines if you change facts, and never delete a "To verify" item without saying how it was resolved.
