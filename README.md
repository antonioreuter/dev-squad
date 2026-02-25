# DevSquad: The Spec-Driven Multi-Agent SDLC

> **Generic AI generates code. DevSquad orchestrates a specialized engineering team to build systems.**

**DevSquad** is an autonomous, collaborative AI orchestration framework. It treats AI Agents not as simple text generators, but as a multidisciplinary **Virtual Engineering Squad** constrained by **Sovereign Domains**, **Operational Logic**, and a **Mandatory Critique Protocol**.

---

## 🏛️ The Philosophy: SDD & Systems Thinking

DevSquad operates on **Spec-Driven Development (SDD)**. The specification isn't just a document; it is the **Single Source of Truth** that every agent audits against.

### Why this matters:

- **Reduces Context Exhaustion**: Agents focus on their domain-specific rules (e.g., Security doesn't care about CSS; UX doesn't care about SQL).
- **Enforces Architectural Integrity**: The "Solution Architect" role acts as a gatekeeper, preventing "Lazy Coding" common in generalist LLMs.
- **Intrinsic Traceability**: Every T001 task is tied to an Acceptance Criterion, which is tied to a Business Requirement.

---

## 🧠 Core Mechanics: Rules, Skills, & Tools

To ensure high-fidelity execution, DevSquad decouples **Identity**, **Capability**, and **Access**.

### 1. Skill-Centric Tooling (The Architecture Pivot)

In DevSquad, Tools (MCP Servers) are not owned by Agents, but by **Skills**. Authorization follows a "Qualified Access" model:

- **Decoupled Infrastructure**: An agent is only authorized to use the `Amazon DynamoDB MCP` if it has adopted the `database-storage-architect` skill for the current task.
- **Result**: Reduced token bloat and zero "hallucinated tool" errors.

### 2. The Devil's Advocate Protocol

Collaboration in DevSquad is built on **Constructive Friction**. Silence is not consent.

- **Mandatory Challenge**: In any multi-agent discussion (e.g., Designing a VPC), one agent MUST act as the Devil's Advocate.
- **Example**:
  - _@AWS-Specialist_: "I propose a public/private subnet split for the API."
  - _@Security-Engineer (Devil's Advocate)_: "Challenge: A public subnet for the API increases the attack surface. Why not use an Internal ALB with Private Link? What's the cost-to-safety trade-off?"

### 3. Decision Hierarchy & ESD

When experts disagree, the system follows a clear escalation path:
`@Human-Leader` > `@Project-Manager` (Strategy) > `@Solution-Architect` (Tech) > **Specialists**.
If a stalemate persists, the highest-ranking agent issues an **Executive Summary Decision (ESD)**—a documented trade-off logged in the project's decision records.

---

## 📂 The "Pointer" Architecture

DevSquad uses a **Lightweight Bridge** strategy to maintain IDE compatibility without context poisoning:

1.  **The Installer**: Deploys the full orchestrator to `.devsquad/`.
2.  **The Pointer**: Generates a small instructions file (e.g., `.cursorrules`, `.windsurfrules`) that tells the IDE: _"You are part of DevSquad. Stop guessing. Read `.devsquad/rules/` before every response."_
3.  **Result**: Your AI stays grounded in your project's specific standards (Hexagonal Architecture, Vitest, AWS CDK).

---

## 🛠️ The Collaborative Workstreams ("Boards")

DevSquad sequences agents through four synchronous milestones:

| Board                 | Focus                  | Active Agents            | Primary Skills                             |
| :-------------------- | :--------------------- | :----------------------- | :----------------------------------------- |
| **1. Hardening**      | Requirements Integrity | PM, Architect, Security  | `ac-review`, `well-architected-reviewer`   |
| **2. Decomposition**  | Atomic Tasking         | PM, Lead Dev             | `task-generator`, `cost-estimator`         |
| **3. Implementation** | Layered Coding         | Lead Dev, AWS Specialist | `lead-developer`, `cloud-designer`         |
| **4. Validation**     | Acceptance Audit       | QA, Security, PM         | `technical-reviewer`, `compliance-auditor` |

---

## 🚀 Quick Start

### 1. Install via UV

The installer probes your OS/IDE and adapts the brain automatically.

```bash
cd dev-squad-cli
uv run dev_squad
```

### 2. Trigger the Loop

- `/squad.plan [idea]` — Turn a raw idea into hardened BDD Acceptance Criteria.
- `/squad.implement [task_id]` — Execute a task with full TDD and architectural rigor.
- `/squad.finish` — Final verification against all quality and safety gates.

---

### 🤝 Squad Participation

- **Agents:** @Solution-Architect, @Project-Manager
- **Skills:** technical-writer
- **Workflows:** none
- **Consensus:** Rewritten to emphasize the specific mechanics of "Skill-Centric Tooling" and "Pointer Architecture."
- **Traceability:** Final response to the documentation consistency gap.
- **Context:** Overhauled the README.md to provide a high-value, systemic overview of the framework, moving away from bulleted lists and towards architectural depth.
