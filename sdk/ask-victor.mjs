#!/usr/bin/env node
// Ask Victor, the Miami real estate advisor, one question with the Claude Agent SDK.
//
// Victor = an agent definition from ../.claude/agents/ (see victor.config.json)
//        + his knowledge folder (persona, skills and research files), added to his system prompt.
//
// Usage:
//   node ask-victor.mjs "Should we sign a Brickell lease at $55/sq ft NNN with rent starting at signing?"
//   node ask-victor.mjs --dry-run "any question"   # load and check Victor without calling the API
//   node ask-victor.mjs --verbose "question"       # also show which tools Victor uses

import { readFileSync, readdirSync, statSync, existsSync } from "node:fs";
import { dirname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { parse as parseYaml } from "yaml";

const HERE = dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = resolve(HERE, "..");

// ---------------------------------------------------------------- arguments
const args = process.argv.slice(2);
const flags = new Set(args.filter((a) => a.startsWith("--")));
const question = args.filter((a) => !a.startsWith("--")).join(" ").trim();
const dryRun = flags.has("--dry-run");
const verbose = flags.has("--verbose");

if (flags.has("--help") || !question) {
  console.error('Usage: node ask-victor.mjs [--dry-run] [--verbose] "your question"');
  process.exit(question ? 0 : 1);
}

// ---------------------------------------------------------------- load config
const config = JSON.parse(readFileSync(join(HERE, "victor.config.json"), "utf8"));
const agentPath = resolve(HERE, config.agentFile);
const knowledgeDir = resolve(HERE, config.knowledgeDir);

function fail(message) {
  console.error(`Error: ${message}`);
  process.exit(1);
}

if (!existsSync(agentPath)) {
  const available = readdirSync(join(PROJECT_ROOT, ".claude", "agents")).filter((f) => f.endsWith(".md"));
  fail(`agent file not found: ${relative(PROJECT_ROOT, agentPath)}\nAvailable agents: ${available.join(", ")}\nFix "agentFile" in sdk/victor.config.json.`);
}
if (!existsSync(join(knowledgeDir, "SKILL.md"))) {
  fail(`knowledge folder not found or has no SKILL.md: ${relative(PROJECT_ROOT, knowledgeDir)}\nFix "knowledgeDir" in sdk/victor.config.json.`);
}

// Split a markdown file into YAML frontmatter and body.
function readMarkdown(path) {
  const text = readFileSync(path, "utf8");
  const match = text.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!match) return { frontmatter: {}, body: text };
  return { frontmatter: parseYaml(match[1]) ?? {}, body: match[2].trim() };
}

// Tools in agent files are a comma-separated string or a YAML list.
function toList(value) {
  if (!value) return [];
  if (Array.isArray(value)) return value.map(String);
  return String(value).split(",").map((s) => s.trim()).filter(Boolean);
}

// ---------------------------------------------------------------- the agent definition
const agentFile = readMarkdown(agentPath);
const { name: sourceName, description, tools: rawTools, skills: listedSkills = [] } = agentFile.frontmatter;
if (!sourceName || !description) fail(`${relative(PROJECT_ROOT, agentPath)} has no name or description in its frontmatter.`);

// Knowledge is added to the prompt directly, and filesystem settings are off,
// so the Skill tool is not needed. Victor may never delegate (no Agent tool).
const tools = toList(rawTools).filter((t) => t !== "Skill" && !t.startsWith("Agent"));

// ---------------------------------------------------------------- the knowledge folder
function listMarkdown(dir) {
  return readdirSync(dir)
    .sort()
    .flatMap((entry) => {
      const full = join(dir, entry);
      if (statSync(full).isDirectory()) return listMarkdown(full);
      return entry.endsWith(".md") ? [full] : [];
    });
}

const persona = readMarkdown(join(knowledgeDir, "SKILL.md"));
const knowledgeFiles = listMarkdown(knowledgeDir).filter((f) => f !== join(knowledgeDir, "SKILL.md"));
const knowledgeText = knowledgeFiles
  .map((f) => `<knowledge_file path="${relative(knowledgeDir, f)}">\n${readFileSync(f, "utf8").trim()}\n</knowledge_file>`)
  .join("\n\n");

const systemPrompt = [
  persona.body,
  "# Your role definition",
  `This comes from the project agent file \`.claude/agents/${relative(join(PROJECT_ROOT, ".claude", "agents"), agentPath)}\`. ` +
    "Where it mentions files under `docs/`, use the copies in your knowledge files under `references/research/`. " +
    "Where it mentions other team agents, the orchestrator or editing project files, follow the Boundaries section above instead: " +
    "you answer the user directly, you do not delegate, and you do not edit files.",
  agentFile.body,
  "# Your knowledge files",
  "These are the full contents of your knowledge folder. Base your answer on them, and list the files you used " +
    "(by their path, for example `references/research/04-startup-and-operating-costs.md`) under **Documents used**.",
  knowledgeText,
].join("\n\n");

const victor = {
  description,
  prompt: systemPrompt,
  tools,
  maxTurns: config.maxTurns ?? 12,
};

// ---------------------------------------------------------------- dry run: show what was loaded
if (dryRun) {
  const summary = {
    agentName: config.agentName,
    loadedFrom: relative(PROJECT_ROOT, agentPath),
    sourceAgentName: sourceName,
    personaFrom: relative(PROJECT_ROOT, join(knowledgeDir, "SKILL.md")),
    personaName: persona.frontmatter?.metadata?.persona ?? null,
    description,
    tools,
    skillsListedInAgentFile: listedSkills,
    knowledgeFiles: knowledgeFiles.map((f) => relative(knowledgeDir, f)),
    systemPromptChars: systemPrompt.length,
    approxSystemPromptTokens: Math.round(systemPrompt.length / 4),
    question,
    anthropicApiKeySet: Boolean(process.env.ANTHROPIC_API_KEY),
  };
  const packaged = new Set(knowledgeFiles.map((f) => relative(knowledgeDir, f).replace(/^references\/skills\//, "").replace(/\.md$/, "")));
  summary.skillsMissingFromKnowledge = listedSkills.filter((s) => !packaged.has(s));
  console.log(JSON.stringify(summary, null, 2));
  const ok = tools.length > 0 && knowledgeFiles.length > 0 && summary.skillsMissingFromKnowledge.length === 0 && /Victor/.test(persona.body);
  console.error(ok ? "Dry run OK: Victor loaded. No API call was made." : "Dry run found problems (see above).");
  process.exit(ok ? 0 : 1);
}

// ---------------------------------------------------------------- ask Victor
if (!process.env.ANTHROPIC_API_KEY) {
  console.error("Warning: ANTHROPIC_API_KEY is not set. The SDK will try any other Claude login on this machine, or fail.");
}

const { query } = await import("@anthropic-ai/claude-agent-sdk");

let answer = null;
let failure = null;
try {
  for await (const message of query({
    prompt: question,
    options: {
      agent: config.agentName, // run the whole session as Victor
      agents: { [config.agentName]: victor },
      tools, // only Victor's tools exist in this session
      allowedTools: tools, // and they run without permission prompts
      settingSources: [], // isolate from the team's CLAUDE.md, settings and other agents
      cwd: PROJECT_ROOT,
      maxTurns: victor.maxTurns,
    },
  })) {
    if (verbose && message.type === "assistant") {
      for (const block of message.message?.content ?? []) {
        if (block.type === "tool_use") console.error(`[tool] ${block.name} ${JSON.stringify(block.input).slice(0, 160)}`);
      }
    }
    if (message.type === "result") {
      if (message.subtype === "success") answer = message.result;
      else failure = `${message.subtype}${message.errors ? ": " + message.errors.join("; ") : ""}`;
    }
  }
} catch (error) {
  failure = error?.message ?? String(error);
}

if (answer) {
  console.log(answer);
} else {
  fail(`Victor did not return an answer (${failure ?? "no result message"}).`);
}
