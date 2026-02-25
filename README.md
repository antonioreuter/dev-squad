# DevSquad: Agentic Spec-Driven Development Platform

> **Transform your AI coding assistant into a multidisciplinary virtual engineering squad.**

DevSquad is an autonomous, collaborative AI orchestration framework designed to revolutionize the software development lifecycle through **Spec-Driven Development (SDD)** and **Systems Thinking**. Unlike traditional auto-coding, DevSquad treats AI agents as a specialized "Virtual Squad" that collaborates, challenges assumptions, and enforces quality gates in real-time.

---

## 🚀 Key Features

- **Virtual Squad**: 12+ specialized agent personas (PM, Solution Architect, AWS Specialists, Security, QA, SRE) with defined sovereignty and competency boundaries.
- **Skill-Centric Tooling**: Decouples MCP tools from agents. Authorization is granted via specialized **Skills**, ensuring least-privilege and reduced cognitive load.
- **Collaborative Intelligence**: A mandatory **Devil's Advocate Protocol** ensures agents critique each other's designs before a single line of code is written.
- **Decision Hierarchy**: Clear protocol for resolving deadlocks with **Executive Summary Decisions (ESD)**.
- **Agnostic & Modular**: Works across Linux, macOS, and Windows. Optimized for **Antigravity**, **Cursor**, and **Windsurf**.

---

## 📂 Project Structure

```bash
.devsquad/
├── rules/       # Always-on behavioral constraints and Agent Mindsets
├── skills/      # On-demand specialist capabilities with associated tools
├── workflows/   # Orchestration scripts (Plan, Implement, Deploy, Observe)
└── mcp.json     # Integration with AWS and external toolsets
```

---

## 🛠️ Quick Start

### 1. Requirements

- Any AI coding assistant (Cursor, Windsurf, Claude Code, etc.)
- [uv](https://docs.astral.sh/uv/) (Python package manager)

### 2. Installation

The DevSquad installer adapts the "Brain" to your specific IDE and OS:

```bash
cd dev-squad-cli
uv run dev-squad
```

### 3. Usage

Trigger the collaborative loop using specialized slash commands:

- `/squad.plan [idea]` — Turn a raw idea into User Stories and AC.
- `/squad.preflight [feature]` — Run the research gate and implementation strategy.
- `/squad.implement [task_id]` — Execute a task with full rules-first rigor and TDD.
- `/squad.observe [service]` — Configure full observability (OTel, SLOs, Alarms).

---

## 🏛️ Core Workflow

1.  **Requirement Hardening**: The Project Manager and Solution Architect challenge your idea to find gaps.
2.  **Task Decomposition**: Atomic, traceable tasks are generated with embedded Acceptance Criteria.
3.  **Autonomous Execution**: Agents implement code layer-by-layer (Domain → Application → Infrastructure).
4.  **Verification**: The QA Tester and Security Engineer audit the output against the "Test Pyramid."

---

## 🤝 Documentation & References

- [TUTORIAL.md](./TUTORIAL.md) — The complete guide to using DevSquad daily.
- [project.md](./project.md) — The full system specification and role roster.
- [todo.md](./todo.md) — Project roadmap and current implementation status.

---

### 🤝 Squad Participation

- **Agents:** @Solution-Architect
- **Skills:** technical-writer
- **Workflows:** none
- **Consensus:** Agreement on the informational structure for the project entry point.
- **Traceability:** Satisfies the final documentation requirement for the "Expansion Plan."
- **Context:** Created the central README.md to provide a high-level overview of the framework and its "Skill-Centric" architecture.
