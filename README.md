# Hi, I'm Dawid

Product guy from Berlin.

I build tools for myself first, then refine what keeps proving useful.
Most things here started from a real need: reducing friction, saving time, or making a recurring task easier to run.

This profile is a working lab for practical software.
You'll find experiments and shipped iterations around AI assistants, automation, and workflow tooling, with a focus on things that are actually usable day to day.

I care about products that stay clear under pressure: clean flows, sensible defaults, and behavior you can trust.
If a project lives here, it solves something concrete and earns its place by being useful in real use.

- Useful over flashy.
- Fast iteration, high standards.
- Simple where it matters, robust where it counts.

## Current focus
- AI skills and copilots for real workflows
- MCP servers that connect AI to local tools
- Infrastructure for autonomous agents

## Repos

**AI Skills** — domain copilots that plug into Claude

| | |
|---|---|
| [collaborate](https://github.com/googlarz/collaborate) | Multi-person document writing skill for Claude — each contributor takes a turn, Claude briefs the next person on what changed, what was tried, and what they need to focus on. Parallel section ownership, structured critique, round robin review. Notifications via Signal or Slack. |
| [finance-assistant](https://github.com/googlarz/finance-assistant) | Personal finance copilot — budgets, investments, debt, taxes, insurance, net worth, multi-currency, bank import (CSV/MT940/OFX), and scenario modeling. Privacy-first: encrypted at rest, runs entirely on your machine. |
| [finance-assistant-locales](https://github.com/googlarz/finance-assistant-locales) | Country plugins for [finance-assistant](https://github.com/googlarz/finance-assistant) — tax rules, social contributions, filing deadlines, deduction logic. Bundled: Germany, UK, France, Netherlands, Poland. US in progress. |
| [health-skill](https://github.com/googlarz/health-skill) | Persistent health workspace for Claude — labs, meds, training, sleep, and family history linked so every conversation builds on the last. Doubles as a longevity companion with check-ins, screenings, and automatic watch sync. |
| [fashion-skill](https://github.com/googlarz/fashion-skill) | Personal AI stylist that actually knows you — derives your color system and fit rules from photos, imports your Zalando/Amazon order history, plans outfits against your calendar and weather, runs Buy/Skip/Only-if checks in-store, audits unworn pieces, and generates Vinted listings to resell them. Honest, not harsh. |
| [math-skill](https://github.com/googlarz/math-skill) | Solver-first math skill — maps the problem, picks the method, derives step-by-step, then double-checks with SymPy before answering. Reads typed problems, photos, whiteboards, and PDFs. |
| [claude-assistant](https://github.com/googlarz/claude-assistant) | Turns Claude Code conversations into context-aware Google Calendar entries — links back to the originating transcript, detects conflicts, finds free slots, auto-inserts prep blocks. The why is right there when the reminder fires. |
| [deterministic-workflow-builder](https://github.com/googlarz/deterministic-workflow-builder) | Compiles vague "make it deterministic" asks into a workflow package — typed `workflow.json` manifest, explicit shell steps, approval gates, contract checks, replayable audits, rollback hooks. AI sidecars stay advisory, never decisive. |
| [deep-context](https://github.com/googlarz/deep-context) | Reads a folder (≤200 files), extracts cited per-file notes, cross-indexes references, runs a red-team pass and self-test calibration, and produces a one-page digest you can actually defend. |
| [logic-audit](https://github.com/googlarz/logic-audit) | Adversarial cross-artifact auditor. Give it code+tests, spec+implementation, prompt+output, or data+chart — surfaces contradictions, broken timelines, identity drift, and unsupported claims. |

**MCP Servers** — real services wired into AI assistants

| | |
|---|---|
| [proton-mail-bridge-client](https://github.com/googlarz/proton-mail-bridge-client) | Local-first Proton Mail for Claude Desktop and terminal — read, search, draft, send, sync, manage, all through Proton Bridge. Never through a cloud relay. CLI + MCP, same backend. |
| [suunto-mcp](https://github.com/googlarz/suunto-mcp) | Talk to your Suunto watch through Claude — runs, hikes, sleep, HR drift, route maps, weekly training summaries. Handles OAuth refresh and FIT-file decoding so you don't have to. CLI + MCP, same backend. _(Awaiting API approval.)_ |
| [signal-mcp](https://github.com/googlarz/signal-mcp) | The most complete Signal MCP server and CLI — 38 tools, quoted replies, @mentions, edit/delete, view-once, full conversation history with FTS5 search, Signal Desktop import. Runs 100% locally via signal-cli. |
| [vinted-client](https://github.com/googlarz/vinted-client) | CLI and MCP server for the Vinted marketplace — search listings, fetch items and sellers, compare prices across countries, pull trending feeds. Stealth-Chromium fallback for full fidelity. |

**Agents & Infrastructure**

| | |
|---|---|
| [scope](https://github.com/googlarz/scope) | Tree-sitter Rust CLI that maps a codebase's structure for LLM agents — what calls what, what tests cover what, what a change touches — before you edit anything. Know before you touch. |
| [agent-skills](https://github.com/googlarz/agent-skills) | Fork of [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) with WIP enhancements: observability skill, CI skill validator, and agent persona integration. Production-grade engineering workflows packaged so AI coding agents follow them every phase — spec, plan, build, test, review, ship. |
| [proactive-claw](https://github.com/googlarz/proactive-claw) | Proactive execution engine for OpenClaw — learns your work style and surfaces prep blocks and follow-ups before you think to ask. Runs fully locally. |
| [stapler](https://github.com/googlarz/stapler) | Fork of [paperclip](https://github.com/paperclipai/paperclip) — self-hosted AI org with per-agent semantic memory (auto-tagged, time-scoped), shared company memory, wiki pages that survive runs, and adapters for Claude, Gemini, Ollama, Codex, OpenCode, Cursor. |
| [claude-code-commands](https://github.com/googlarz/claude-code-commands) | Complete reference of every `/` command in Claude Code (v2.1.92) — built-ins, bundled skills, hidden/dev-only, removed, plus visibility and enablement rules. Extracted from the macOS binary. |

## Notes
- Built from personal use-cases
- Iterated in public
- Kept practical
