# How to Talk to Your Experts

There are three ways to ask the Experts21 team a question:

| You want… | Use | Who answers |
|---|---|---|
| A combined answer to a question that needs several experts | The **orchestrator** | The orchestrator picks 2–6 experts, runs them, has them cross-check each other, and returns one answer |
| A quick answer from one specialist | **One expert agent** | That expert only |
| A review from every relevant part of the team | The **orchestrator**, asked for a full-team review | The orchestrator runs the experts in waves and returns one consolidated report |

All agent names are listed in [expert-roster.md](expert-roster.md). Setup is explained in [`CLAUDE.md`](../CLAUDE.md).

---

## 1. Questions the whole team works on together (through the orchestrator)

Start a session where every message goes to the orchestrator:

```bash
claude --agent orchestrator
```

Then paste one of these prompts. Under each one you'll see which experts the orchestrator is likely to bring in, based on its routing map. It decides the final set itself.

### Example A: Choosing a location
> We're choosing between Brickell and Coral Gables for our first café, about 1,200 sq ft with 30 seats. Which neighborhood should we pick, and what's the realistic monthly rent, break-even and biggest risk in each? Give me a recommendation I can take to the client.

**Likely experts:**
- `site-selection` (lead)
- `competitive-intel`
- `customer-insights`
- `financial-modeler`
- `permits-expeditor`
- `risk-manager`
- `red-team-reviewer` (this is a high-stakes decision)

**You get:** one recommendation, a side-by-side comparison of the two neighborhoods, break-even transactions per day for each, and the risks, plus a proposed entry in `decision-log.md`.

### Example B: Reviewing a lease offer
> A landlord on Calle Ocho offered us 1,000 sq ft at $38/sq ft NNN, a 5-year term, a full personal guarantee, rent starting at signing and no tenant-improvement allowance. The space was a restaurant before. Should we take it? What should we counter with, and how does it change our budget?

**Likely experts:**
- `lease-counsel` (lead)
- `site-selection`
- `financial-modeler`
- `permits-expeditor`
- `buildout-manager`
- `red-team-reviewer`

**You get:** a red/amber/green read of each lease term, a counter-proposal (permit contingency, rent starting once the Certificate of Use is issued, free rent, a limited guarantee), the real occupancy cost as a share of revenue, and an updated startup budget.

### Example C: Budget and funding plan
> Build me the full opening budget for a Cuban-meets-specialty café with a walk-up ventanita window, and tell me how much cash we need in total, how to fund it (savings vs. SBA loan vs. equipment financing), and the month we'd run lowest on cash in a downside case.

**Likely experts:**
- `financial-modeler` (lead)
- `concept-designer`
- `equipment-specialist`
- `buildout-manager`
- `funding-advisor`
- `tax-accountant`
- `red-team-reviewer`

**You get:** a startup budget broken into categories, a 36-month cash view with base and downside cases, the recommended mix of funding sources, and the assumptions that most need real quotes.

### Example D: Opening-season plan
> We want to open next October. Give me a launch plan for the first six months: menu and prices, staffing and schedule, marketing for opening and Art Basel, and how we get through hurricane season and the summer slump without running out of cash.

**Likely experts:**
- `engagement-lead` (lead, writes the plan)
- `menu-developer`
- `head-of-coffee`
- `workforce-planner`
- `hr-talent`
- `brand-strategist`
- `community-partnerships`
- `risk-manager`
- `financial-modeler`

**You get:** a dated plan with owners, the opening menu and price list, a staffing model with labor %, a marketing calendar, the hurricane and summer playbook, and open items.

### Tips for prompts like these
- **Give the facts you know:** size, budget, neighborhood, dates, offers on the table. The experts start fresh and only know what you, `docs/` and the decision log tell them.
- **Say what you need back:** for example "a recommendation I can take to the client", "under 300 words" or "a table".
- **Name experts if you want them:** for example "Make sure the red team reviews this." The orchestrator adds them.
- **Record decisions:** ask "Record this in the decision log as proposed." Then ask `engagement-lead` to mark it decided once the client agrees.

### Without starting a special session
In a normal `claude` session, any of these also works:
```text
Use the orchestrator subagent: should we open in Brickell or Coral Gables?
```
```text
@agent-orchestrator review this lease offer: …
```

---

## 2. Asking one specific agent

Use this for narrow questions in one expert's area. It's faster and cheaper than a team answer.

**@-mention the agent** in any session (type `@` and pick it, or type it out):
```text
@agent-permits-expeditor What permits do we need for a 30-seat café in the City of Miami, in what order, and how long will it take?
```
```text
@agent-head-of-coffee Shortlist three Miami roasters we could partner with and how you'd compare them.
```
```text
@agent-cultural-advisor Is "Ventanita & Co." a good name for our shop in English and Spanish?
```

**Or name it in plain language:**
```text
Use the financial-modeler subagent to recompute break-even if rent is $7,500 a month.
```

**Or start a whole session as that expert** (useful for a long working session with one specialist):
```bash
claude --agent financial-modeler
```

**Or ask once from the shell** (prints the answer and exits):
```bash
claude -p --agent menu-developer "Cost a 12 oz oat latte and suggest a price."
```

Experts don't call each other. If part of your question belongs to someone else, the expert tells you who; ask that agent next, or send the question to the orchestrator.

---

## 3. Asking the whole team

To hear from every relevant part of the team, ask the orchestrator for a **full-team review**. It runs the experts in waves: up to 20 agents can run at once, so it won't start all 31 together. Then it returns one consolidated report.

```bash
claude --agent orchestrator
```
```text
Full-team review: here is our current plan (Cuban-meets-specialty café, ~1,200 sq ft in Brickell,
$320K budget, opening October). Run it past every relevant expert in waves
(strategy and customers; site, lease and permits; product and operations; people;
finance and funding; marketing; risk), then have the red team challenge the result.
Give me one report: overall verdict, top 10 issues ranked, what each domain recommends,
disagreements and how you resolved them, and the next 5 actions with owners.
```

**Good to know:**
- A full-team review takes several minutes and uses far more tokens than a normal question. Use it at milestones, such as before signing a lease or before applying for a loan, not for everyday questions.
- To keep it smaller, list the domains you want, for example "only finance, legal and risk".
- If the review leads to a decision, ask for it to be added to `docs/decision-log.md`.

---

## 4. Changing the team itself

Changes to the team go to the `meta-agent`, not the orchestrator:
```text
@agent-meta-agent Add a "Grants & Incentives" expert for Miami-Dade small-business programs, give it a matching skill, and wire it into the orchestrator.
```
```text
@agent-meta-agent The site-selection agent keeps forgetting parking. Improve it.
```

The meta-agent updates the agent and skill files, the roster and `CLAUDE.md`, then runs the validator.

## Troubleshooting
| Problem | Fix |
|---|---|
| The orchestrator says it can't call experts | Your environment has turned off nesting (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`). Use `claude --agent orchestrator` so the experts run one level down. |
| Experts say they couldn't search the web | Allow `WebSearch` and `WebFetch` when prompted, or add them to your permissions. Otherwise they work only from `docs/`. |
| The answer is too long | Say how long you want it, e.g. "under 200 words" or "one table". |
| Wrong experts were picked | Name the ones you want, or ask `meta-agent` to improve the routing map. |
