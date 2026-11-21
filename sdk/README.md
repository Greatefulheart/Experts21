# Ask Victor (Claude Agent SDK)

A small Node.js script that loads **Victor**, the Miami real estate advisor, and asks him one question from the command line. It uses the [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview) (`@anthropic-ai/claude-agent-sdk`).

## What gets loaded
| Part | From | Notes |
|---|---|---|
| Agent definition (description, tools, role instructions) | `.claude/agents/site-selection.md` | The project has no separate `real-estate-advisor` agent file. Victor was built from `site-selection`, the team's "Site Selection & Real Estate Advisor". |
| Persona and knowledge folder | `exports/victor-real-estate-advisor/` | `SKILL.md` (Victor's personality and instructions), 9 skill files, and 8 research files |

Both paths are set in [`victor.config.json`](victor.config.json). If you later add a dedicated agent file such as `.claude/agents/real-estate-advisor.md`, change `agentFile` to point at it.

How the script uses the SDK:
- The agent file is parsed into an SDK `AgentDefinition`. The SDK runs the whole session as that agent (`agent: "victor"`).
- The knowledge files go straight into Victor's system prompt (about 15K tokens), so he can cite them by path.
- `settingSources: []` keeps the rest of the project (the team's `CLAUDE.md`, settings and the other 32 agents) out of the session.
- Victor can use only `Read`, `Grep`, `Glob`, `WebSearch` and `WebFetch`, pre-approved. He can't edit files, run commands or delegate.

## Requirements
- Node.js 18 or later (tested with Node 22)
- An Anthropic API key from https://console.anthropic.com/

## Install
From the project root:
```bash
cd sdk
```
```bash
npm install
```

## Set your API key
macOS / Linux:
```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```
Windows PowerShell:
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-your-key-here"
```
Don't commit your key or paste it into project files.

## Run
Ask a question (inside `sdk/`):
```bash
node ask-victor.mjs "Should we sign a Brickell lease at \$55/sq ft NNN with rent starting at signing and a full personal guarantee? What are the top three things to negotiate? Tell me which documents you used."
```
Or through npm:
```bash
npm run ask -- "Which is better for our first café, Brickell or Coral Gables?"
```
To also see which tools Victor uses while he works (printed to stderr):
```bash
node ask-victor.mjs --verbose "What rent per square foot should we budget for Little Havana?"
```
The answer is printed to stdout, so you can save it:
```bash
node ask-victor.mjs "Score a 1,200 sq ft second-generation café space in Edgewater" > victor-answer.md
```

## Check that Victor loads (no API call, no key needed)
```bash
npm run check
```
This prints what was loaded (agent file, persona, tools, the 17 knowledge files, prompt size) and exits with code 0 if Victor is complete. It makes no API call.

## Troubleshooting
| Problem | Fix |
|---|---|
| `agent file not found` | Fix `agentFile` in `victor.config.json`. The error lists the available agents. |
| `knowledge folder not found` | Fix `knowledgeDir`, or rebuild the package in `exports/victor-real-estate-advisor/`. |
| Authentication error | Check that `ANTHROPIC_API_KEY` is set in the same terminal: `echo $ANTHROPIC_API_KEY` |
| `error_max_turns` | Raise `maxTurns` in `victor.config.json`. |
| Answers lack current market data | Web search depends on your account and network. Without it, Victor answers from his knowledge files and says what needs verifying. |

Victor's guidance is research-grade. A licensed Florida real estate attorney must review any lease before it is signed.
