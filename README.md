# Dawid Piaskowski

Would you give an AI your inbox, your bank statements and your lab results? Only if none of it ever leaves your machine.

I'm a product guy in Berlin, and I build exactly that: **local-first tools that let Claude work with your real data**: mail, messages, money, health, training.

![npm downloads](https://img.shields.io/npm/dm/proton-mail-bridge-client?label=proton-mail-bridge-client%20downloads%2Fmonth) ![PyPI](https://img.shields.io/pypi/v/signal-mcp?label=signal-mcp) ![npm](https://img.shields.io/npm/v/suunto-mcp?label=suunto-mcp)

**5 MCP servers · 96 tools in the biggest one · ~10k npm downloads a month · everything runs on your machine**

<p align="center">
  <a href="https://github.com/googlarz/duo">
    <img src="https://raw.githubusercontent.com/googlarz/duo/main/assets/duo-panel-running.png" alt="duo: a live panel of every agent Claude Code spawns, with model, effort, steps, tokens and usage limit" width="709">
  </a>
  <br>
  <sub><b><a href="https://github.com/googlarz/duo">duo</a></b>: see every agent Claude spawns, live.</sub>
</p>

## Start here

| Project | What it does | Get it |
| --- | --- | --- |
| **[proton-mail-bridge-client](https://github.com/googlarz/proton-mail-bridge-client)** | Proton Mail for Claude via Proton Bridge. Up to 96 MCP tools plus a CLI. Read, search, draft, send, with read-only and send-to-self modes. | `npm i -g proton-mail-bridge-client` |
| **[finance-assistant](https://github.com/googlarz/finance-assistant)** | Personal finance copilot for Claude Code. Bank imports, country-specific tax rules, scenario modelling. 1,100+ test functions. | [see README](https://github.com/googlarz/finance-assistant) |
| **[signal-mcp](https://github.com/googlarz/signal-mcp)** | Signal for Claude via signal-cli, with local history and full-text search. 79 MCP tools. | `pipx install signal-mcp` |
| **[suunto-mcp](https://github.com/googlarz/suunto-mcp)** | Ask Claude about your Suunto workouts, sleep and recovery, and push workouts back to the watch. 24 MCP tools. | `npx -y suunto-mcp` |
| **[duo](https://github.com/googlarz/duo)** | Claude Code plugin that shows every agent Claude spawns: task, model, effort, steps, tokens, usage limit. Fork of JohnnyVizz's claude-kit. | `/plugin marketplace add googlarz/duo` |
| **[LLMessenger](https://github.com/googlarz/LLMessenger)** | macOS app that digests iMessage, Signal, Telegram and Slack on-device and drafts replies for your approval. | [see README](https://github.com/googlarz/LLMessenger) |

## Recently shipped

<!-- RECENT:START -->
- [proton-mail-bridge-client v2.17.1](https://github.com/googlarz/proton-mail-bridge-client/releases/tag/v2.17.1) — Local-first Proton Mail MCP server and CLI via Proton Bridge. Search, draft, send and organize ma... · 2026-10-30
- [finance-assistant v4.2.1](https://github.com/googlarz/finance-assistant/releases/tag/v4.2.1) — Personal finance copilot — real math, not AI guesses. 6 locales · 13 bank formats · Monte Carlo F... · 2026-10-30
- [finance-assistant-locales v2.6.0](https://github.com/googlarz/finance-assistant-locales/releases/tag/v2.6.0) — Locale plugins for Finance Assistant — country-specific tax rules, social contributions, filing d... · 2026-10-30
- [suunto-mcp v0.21.0](https://github.com/googlarz/suunto-mcp/releases/tag/v0.21.0) — MCP server that connects your Suunto watch data to Claude and other AI assistants · 2026-10-29
- [signal-mcp v1.43.3](https://github.com/googlarz/signal-mcp/releases/tag/v1.43.3) — Signal for AI assistants: an MCP server + CLI with searchable local message history, groups, poll... · 2026-10-21
- [vinted-mcp-cli v1.6.3](https://github.com/googlarz/vinted-mcp-cli/releases/tag/v1.6.3) — Browse, search, and manage Vinted listings from Claude or the terminal — buy, sell, track items,... · 2026-10-07
<!-- RECENT:END -->

## More

- **Personal skills for Claude:** [health-skill](https://github.com/googlarz/health-skill) · [suunto-gym](https://github.com/googlarz/suunto-gym) · [fashion-skill](https://github.com/googlarz/fashion-skill) · [personal-inbox](https://github.com/googlarz/personal-inbox)
- **Skills for working with Claude Code:** [duo](https://github.com/googlarz/duo) · [delegate](https://github.com/googlarz/delegate) · [vibe-safe](https://github.com/googlarz/vibe-safe) · [logic-audit](https://github.com/googlarz/logic-audit) · [deep-context](https://github.com/googlarz/deep-context) · [context-handoff](https://github.com/googlarz/context-handoff) · [agents-sync](https://github.com/googlarz/agents-sync)
- **Other MCP servers:** [proton-drive-mcp](https://github.com/googlarz/proton-drive-mcp) · [vinted-mcp-cli](https://github.com/googlarz/vinted-mcp-cli)

## How I build

- Private by default: local storage, no telemetry, read-only modes where possible.
- Built for my own use first, then released once it holds up.
- Honest about limits: finance and health tools are assistants, not licensed advice.

[LinkedIn](https://www.linkedin.com/in/dawidpiaskowski) · [All repositories](https://github.com/googlarz?tab=repositories)
