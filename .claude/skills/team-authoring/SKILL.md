---
name: team-authoring
description: "Create, change and validate this project's Claude Code subagents and skills: file formats, frontmatter fields, naming, wiring agents to skills, roster and routing-map upkeep, and the validator script."
when_to_use: "Use when adding, editing, merging, renaming or removing an agent or skill in this project, or when checking the team definitions are valid."
---

# Team authoring

Follow the official docs: https://code.claude.com/docs/en/sub-agents and https://code.claude.com/docs/en/skills (re-read them with WebFetch if behavior seems to have changed).

## Agent files: `.claude/agents/<agent-id>.md`
- First line must be `---`. Required frontmatter: `name` (lowercase-hyphen, no `:`, unique) and `description` (when to delegate; start with the role, include "Use for/when ..." triggers; keep it under ~60 words, because all descriptions share a 15,000-token budget).
- Optional fields used here: `tools` (comma-separated allowlist), `skills` (YAML list of skill ids to preload; max 32; full content is injected, so keep the list focused), `model`, `effort`, `color`. Field names are case-sensitive; unknown fields are silently ignored.
- Expert agents must NOT list `Agent` in `tools` (only the orchestrator delegates). Experts get `Read, Grep, Glob, WebSearch, WebFetch, Skill` (+ `Bash` for quantitative roles). Only `orchestrator`, `engagement-lead` and `meta-agent` get `Write`/`Edit`.
- Body = system prompt. Use the existing experts as the template: identity and mission; context (key docs); responsibilities; how to work; output (standard expert response format); boundaries; who to name for hand-offs.

## Skill files: `.claude/skills/<skill-id>/SKILL.md`
- Frontmatter: `name` (same as the directory), `description` (what it does, key use first), `when_to_use` (triggers). description + when_to_use must stay under 1,536 characters. Do not set `disable-model-invocation: true` on skills that agents preload.
- Body: purpose, inputs (which docs), procedure, output format, rules and checks. Keep it under ~150 lines; put long reference material in supporting files next to SKILL.md and link them.

## When you add or change an agent
1. Write or edit the agent file and preload the right skills.
2. If it is an expert: add it to the orchestrator's `tools: Agent(...)` list and to the routing map in `multi-agent-coordination`.
3. Update `docs/expert-roster.md` (agent table, skills "Used by" column, reverse index, counts) and the team table in `CLAUDE.md`.

## When you add or change a skill
1. Write the skill; add it to each user's `skills` list.
2. Update `docs/expert-roster.md`.

## Validate
Run `python3 .claude/skills/team-authoring/scripts/validate_team.py` from the project root and fix every error. It checks frontmatter, names, skill wiring, description length, tool rules, the orchestrator allowlist and the roster.

## Quality bar for improvements
Specific to the Miami coffee project, grounded in `docs/`, actionable steps, clear output format, no overlap without a stated reason, no invented facts.
