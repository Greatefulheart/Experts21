# Experts21: advisory agent team for a Miami specialty coffee shop

This project is a team of Claude Code agents that advises a consultant on opening an independent **specialty coffee shop in Miami, Florida**. The research the team works from is in `docs/`. The team itself is in `.claude/`.

## Layout
| Path | What it is |
|---|---|
| `docs/README.md`, `docs/01-…08-*.md` | Research pack: market, customers, competitors, costs, permits, staffing, marketing, risks |
| `docs/expert-roster.md` | Every agent and skill, with which agent uses which skill |
| `docs/decision-log.md` | Decisions taken (proposed or decided) |
| `.claude/agents/*.md` | 33 project subagents: 31 experts, plus `orchestrator` and `meta-agent` |
| `.claude/skills/*/SKILL.md` | 39 shared skills, preloaded into agents through their `skills:` field |
| `.claude/skills/team-authoring/scripts/validate_team.py` | Checks that the team's files are consistent |
| `.claude/settings.json` | Sets the subagent nesting depth to 2 so the orchestrator can run experts when it is itself a subagent |

## The team
- **`orchestrator`** is the entry point. It takes any question, picks the experts, runs them (in parallel where it can), has them cross-check each other, and returns one combined answer.
- **31 experts** in 11 domains: leadership (`engagement-lead`, `red-team-reviewer`), business and strategy, coffee and product, real estate and build, technical, operations, people, finance, legal, marketing, and risk. See `docs/expert-roster.md` for each one's job and skills.
- **`meta-agent`** creates new agents and skills, improves existing ones, and keeps everything in sync.

## How to use it
1. **Recommended:** start a session as the orchestrator. Every question then goes through the team:
   ```bash
   claude --agent orchestrator
   ```
2. In a normal session, ask for it: "Use the orchestrator subagent: should we open in Brickell or Coral Gables?" or type `@agent-orchestrator`.
3. Ask one expert directly for a narrow question, for example `@agent-financial-modeler`, `@agent-permits-expeditor` or `@agent-head-of-coffee`.
4. Change the team: "Use the meta-agent to add a roastery-operations expert" (or to improve, merge or retire an agent or skill).

## Rules for every agent
- Read the relevant files in `docs/` first, and check `docs/decision-log.md` before recommending anything.
- Label numbers as **Fact** (with source and date), **Estimate**, **Assumption** or **To verify**. Never invent facts, sources or fees.
- Experts answer in the standard expert response format (defined in the `docs-knowledge-base` skill). They do not delegate and do not edit `docs/`; they propose changes instead.
- Only `orchestrator`, `engagement-lead` and `meta-agent` edit files. Decision-log entries are added, never rewritten.
- Legal, tax, insurance, permit and engineering guidance is research-grade. A licensed professional or the relevant agency must confirm it before anything is signed, filed or built.

## Changing the team
Use `meta-agent`, or follow the `team-authoring` skill by hand. When you add or rename an agent or skill, also update:
- the orchestrator's `Agent(...)` allowlist,
- the routing map in `.claude/skills/multi-agent-coordination/SKILL.md`,
- `docs/expert-roster.md`,
- this file.

Then run:
```bash
python3 .claude/skills/team-authoring/scripts/validate_team.py
```

## Notes
- Subagents start without this conversation's history. The orchestrator writes each expert a self-contained brief.
- If nesting is turned off in your environment (`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1`), run the orchestrator as the main session (option 1) so it can still start the experts.
- Experts use `WebSearch` and `WebFetch` for current facts. Allow those tools, or the experts will work only from `docs/`.
