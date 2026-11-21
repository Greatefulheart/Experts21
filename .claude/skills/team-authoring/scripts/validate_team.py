#!/usr/bin/env python3
"""Validate the Experts21 agent team: agent files, skill files, wiring, orchestrator allowlist and roster.

Run from the project root:  python3 .claude/skills/team-authoring/scripts/validate_team.py
Exit code 0 = no errors (warnings may still be printed).
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
AGENTS_DIR = os.path.join(ROOT, ".claude", "agents")
SKILLS_DIR = os.path.join(ROOT, ".claude", "skills")
ROSTER = os.path.join(ROOT, "docs", "expert-roster.md")
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
DELEGATORS = {"orchestrator"}
WRITERS = {"orchestrator", "engagement-lead", "meta-agent"}

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def parse_frontmatter(path):
    """Minimal YAML subset parser: `key: value`, quoted strings, and `key:` followed by `  - item` lists."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None, text
    data, key = {}, None
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^\s+-\s+(.*)$", line)
        if m and key:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(m.group(1).strip().strip('"\''))
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if not m:
            err(f"{os.path.relpath(path, ROOT)}: cannot parse frontmatter line: {line!r}")
            continue
        key, val = m.group(1), m.group(2).strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1].encode().decode("unicode_escape") if "\\" in val else val[1:-1]
        elif val.startswith("'") and val.endswith("'"):
            val = val[1:-1]
        data[key] = val if val != "" else []
    return data, "\n".join(lines[end + 1:])


def split_tools(s):
    if isinstance(s, list):
        return s
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur.strip())
    return out


# ---------------- skills
skills = {}
if not os.path.isdir(SKILLS_DIR):
    err("missing .claude/skills/")
else:
    for d in sorted(os.listdir(SKILLS_DIR)):
        p = os.path.join(SKILLS_DIR, d, "SKILL.md")
        if not os.path.isdir(os.path.join(SKILLS_DIR, d)):
            continue
        if not os.path.exists(p):
            err(f"skill dir {d}/ has no SKILL.md")
            continue
        fm, body = parse_frontmatter(p)
        rel = os.path.relpath(p, ROOT)
        if fm is None:
            err(f"{rel}: frontmatter must start on line 1 with ---")
            continue
        name = fm.get("name", d)
        if name != d:
            err(f"{rel}: name '{name}' should equal directory '{d}'")
        if not NAME_RE.match(d):
            err(f"{rel}: directory name should be lowercase-hyphen")
        desc = fm.get("description", "")
        if not desc:
            err(f"{rel}: missing description")
        total = len(desc) + len(fm.get("when_to_use", "") or "")
        if total > 1536:
            err(f"{rel}: description + when_to_use is {total} chars (limit 1536)")
        if str(fm.get("disable-model-invocation", "")).lower() in ("true", "yes", "on", "1"):
            warn(f"{rel}: disable-model-invocation is set; agents cannot preload it")
        if len(body.strip()) < 200:
            warn(f"{rel}: body looks very short")
        if body.count("\n") > 300:
            warn(f"{rel}: body over 300 lines; move reference material to supporting files")
        skills[d] = fm

# ---------------- agents
agents = {}
if not os.path.isdir(AGENTS_DIR):
    err("missing .claude/agents/")
else:
    for root, _, files in os.walk(AGENTS_DIR):
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, ROOT)
            fm, body = parse_frontmatter(p)
            if fm is None:
                err(f"{rel}: frontmatter must start on line 1 with ---")
                continue
            name = fm.get("name")
            if not name:
                err(f"{rel}: missing name")
                continue
            if not NAME_RE.match(name) or ":" in name or len(name) > 256:
                err(f"{rel}: invalid name '{name}'")
            if name in agents:
                err(f"{rel}: duplicate agent name '{name}'")
            if not fm.get("description"):
                err(f"{rel}: missing description")
            elif len(fm["description"].split()) > 90:
                warn(f"{rel}: description is {len(fm['description'].split())} words; keep it short")
            if fn[:-3] != name:
                warn(f"{rel}: filename differs from name '{name}'")
            sk = fm.get("skills", [])
            if isinstance(sk, str):
                sk = [s.strip() for s in sk.split(",") if s.strip()]
            if len(sk) > 32:
                err(f"{rel}: {len(sk)} skills listed; only the first 32 are preloaded")
            for s in sk:
                if s not in skills:
                    err(f"{rel}: skill '{s}' does not exist in .claude/skills/")
            if "docs-knowledge-base" not in sk:
                warn(f"{rel}: does not preload docs-knowledge-base")
            tools = split_tools(fm.get("tools", "")) if fm.get("tools") else None
            fm["_tools"] = tools
            fm["_skills"] = sk
            if tools is not None:
                has_agent = any(t == "Agent" or t.startswith("Agent(") for t in tools)
                if has_agent and name not in DELEGATORS:
                    err(f"{rel}: only the orchestrator may have the Agent tool")
                if any(t in ("Write", "Edit") for t in tools) and name not in WRITERS:
                    warn(f"{rel}: has Write/Edit; experts normally propose doc changes instead")
            if len(body.strip()) < 300:
                warn(f"{rel}: system prompt looks very short")
            agents[name] = fm

# ---------------- orchestrator allowlist
experts = [a for a in agents if a not in ("orchestrator", "meta-agent")]
orch = agents.get("orchestrator")
if not orch:
    err("orchestrator agent missing")
else:
    allowed = set()
    for t in orch.get("_tools") or []:
        m = re.match(r"^Agent\((.*)\)$", t)
        if m:
            allowed |= {x.strip() for x in m.group(1).split(",") if x.strip()}
    for e in experts:
        if e not in allowed:
            err(f"orchestrator: expert '{e}' missing from tools Agent(...) allowlist")
    for x in allowed - set(experts):
        err(f"orchestrator: Agent(...) allowlist names unknown or non-expert agent '{x}'")
    rmap = os.path.join(SKILLS_DIR, "multi-agent-coordination", "SKILL.md")
    if os.path.exists(rmap):
        text = open(rmap, encoding="utf-8").read()
        for e in experts:
            if not re.search(rf"(?<![\w-]){re.escape(e)}(?![\w-])", text):
                warn(f"routing map in multi-agent-coordination does not mention '{e}'")
if "meta-agent" not in agents:
    err("meta-agent missing")

# ---------------- unused skills
used = {s for a in agents.values() for s in a.get("_skills", [])}
for s in skills:
    if s not in used:
        warn(f"skill '{s}' is not preloaded by any agent")

# ---------------- roster
if not os.path.exists(ROSTER):
    err("docs/expert-roster.md missing")
else:
    roster = open(ROSTER, encoding="utf-8").read()
    for a in agents:
        if f"`{a}`" not in roster:
            err(f"roster: agent '{a}' not listed in docs/expert-roster.md")
    for s in skills:
        if f"`{s}`" not in roster:
            err(f"roster: skill '{s}' not listed in docs/expert-roster.md")
    m = re.search(r"\*\*(\d+) agents\*\*", roster)
    if m and int(m.group(1)) != len(agents):
        err(f"roster: says {m.group(1)} agents, found {len(agents)}")
    m = re.search(r"\*\*(\d+) shared skills\*\*", roster)
    if m and int(m.group(1)) != len(skills):
        err(f"roster: says {m.group(1)} skills, found {len(skills)}")
    # reverse index must match frontmatter
    for line in roster.split("\n"):
        m = re.match(r"^\|[^|]*\|\s*`([a-z0-9-]+)`\s*\|\s*(`[^|]*)\|\s*$", line)
        if m and m.group(1) in agents:
            listed = re.findall(r"`([a-z0-9-]+)`", m.group(2))
            if set(listed) != set(agents[m.group(1)].get("_skills", [])):
                err(f"roster: reverse-index skills for '{m.group(1)}' differ from its agent file")

print(f"Agents: {len(agents)} ({len(experts)} experts)  Skills: {len(skills)}")
for w_ in warnings:
    print("WARNING:", w_)
for e in errors:
    print("ERROR:", e)
if not (10 <= len(agents) <= 50):
    print(f"WARNING: team size {len(agents)} is outside the 10–50 target")
print("OK" if not errors else f"FAILED with {len(errors)} error(s)")
sys.exit(1 if errors else 0)
