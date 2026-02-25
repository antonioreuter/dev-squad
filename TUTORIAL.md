# DevSquad: The Complete Tutorial

> Your Virtual Engineering Squad, powered by AI. From idea to production-ready code — with critical thinking, quality gates, and zero fluff.

---

## Table of Contents

1. [What is DevSquad?](#1-what-is-devsquad)
2. [Core Concepts](#2-core-concepts)
3. [Installation](#3-installation)
4. [The Squad — Who's in the Room?](#4-the-squad--whos-in-the-room)
5. [The Workflow — From Idea to Code](#5-the-workflow--from-idea-to-code)
6. [Skills Reference — On-Demand Intelligence](#6-skills-reference--on-demand-intelligence)
7. [Rules Reference — Always-On Standards](#7-rules-reference--always-on-standards)
8. [Daily Usage Patterns](#8-daily-usage-patterns)
9. [Reading the Squad's Output](#9-reading-the-squads-output)
10. [Customizing for Your Project](#10-customizing-for-your-project)

---

## 1. What is DevSquad?

DevSquad transforms your AI coding assistant into a **multidisciplinary engineering team**. Instead of a single AI that tries to do everything, DevSquad provides specialized agent personas — each with a defined domain, a critical thinking mandate, and strict competency boundaries.

**The result**: You get a Solution Architect who challenges your scalability assumptions, a Security Engineer who treats every input as malicious, and a QA Tester who asks "what if?" before you write a line of code — all working together on your feature from the first idea.

### What DevSquad is NOT

- ❌ A rigid bureaucratic process generator (no forced templates)
- ❌ A replacement for your judgment as the Human Leader
- ❌ Tied to any specific IDE, model, or cloud provider

### What DevSquad IS

- ✅ A **collaborative intelligence layer** layered on top of your existing AI assistant
- ✅ A set of **always-on behavioral rules** that prevent common engineering mistakes
- ✅ A **structured workflow** from idea → spec → tasks → code → done

---

## 2. Core Concepts

Understanding these three building blocks is all you need to use DevSquad effectively.

### 🗂️ Rules (Always Active)

Rules are behavioral constraints that are **always active** — your AI agent reads them before every response. They define:

- Standards (coding, architecture, security, API design)
- Role mindsets (who thinks what, and about what domain)
- Interaction protocols (how agents communicate with each other and with you)

You never explicitly "call" a rule. They are the squad's shared operating principles.

### 🔌 Tools & MCP (Skill-Owned)

In DevSquad, Tools (like MCP Servers) are not owned by Agents, but by **Skills**. An Agent is authorized to use a tool only if it has adopted a Skill that requires it. This minimizes context bloat and ensures the AI focuses only on the tools relevant to its current task.

### 🛠️ Skills (On-Demand)

Skills are **specialist capabilities** you invoke when you need them. They are triggered by describing what you want, or by referencing the skill name in your prompt. Examples:

- "Run an `/ac-review` on these acceptance criteria"
- "Use `task-generator` to break this down"
- "Apply `compliance-auditor` to this user data module"

### ⚙️ Workflows (Orchestration Scripts)

Workflows are **structured multi-step processes** triggered by a slash command. They orchestrate multiple agents and skills toward a specific milestone.

| Command                         | Purpose                                                  |
| ------------------------------- | -------------------------------------------------------- |
| `/squad.plan [idea]`            | Turn a raw idea into User Stories + Acceptance Criteria  |
| `/squad.preflight [feature]`    | Pre-flight check + research gate before writing code     |
| `/squad.implement [task_id]`    | Execute a single atomic task with strict TDD             |
| `/squad.finish [feature]`       | Quality wrap-up + hand-off to review                     |
| `/squad.deploy [service?]`      | Full safe release to production                          |
| `/squad.observe [service]`      | Set up full observability (OTel, SLOs, alarms, RUM)      |
| `/squad.incident [description]` | Structured incident response: triage → RCA → post-mortem |

---

## 3. Installation

### Requirements

- Any AI coding assistant (Antigravity, Cursor, Windsurf, VSCode, Claude Code, etc.)
- Git
- The [uv](https://docs.astral.sh/uv/) Python package manager

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-org/dev-squad.git
cd dev-squad
```

### Step 2 — Run the Installer

The DevSquad CLI wizard is built in Python and runs smoothly via `uv`:

```bash
cd dev-squad-cli
uv run dev-squad
```

### Step 3 — Answer the Wizard

The installer will ask you **four questions**:

```
  ______           _____
 |  __  \         / ____|
 | |  | | _____  | (___   __ _ _   _  __ _  __| |
 | |  | |/ _ \ \ / \___ \ / _` | | | |/ _` |/ _` |
 | |__| |  __/ V / ____) | (_| | |_| | (_| | (_| |
 |_____/ \___| \_/ |_____/ \__, |\__,_|\__,_|\__,_|
                               | |
                               |_|  Agentic SDD Framework

Welcome to the DevSquad Installer Wizard!
--------------------------------------------------------

Step 1: Select your Operating System
1) Linux
2) macOS
3) Windows
Choose an option [1-3]:

Step 2: Select your target IDE
1) VSCode
2) Windsurf
3) Cursor
4) Antigravity
5) Terminal / CLI
Choose an option [1-5]:

Step 3: Select your AI Model / Agent Extension
1) IDE Native (Built-in)
2) Claude Code
3) GitHub Copilot
4) RooCode (Cline)
Choose an option [1-4]:

Step 4: Select MCP Servers to Enable (Space to select, Enter to confirm)
instructions: ...
❯ ◯ AWS Documentation MCP Server
  ◯ AWS IaC MCP Server
  ◯ AWS Lambda MCP Server
  ◯ AWS Serverless MCP Server
  ◯ AWS Pricing MCP Server
  ◯ CloudWatch MCP Server
  ◯ CloudWatch Application Signals MCP Server
  ◯ AWS Well-Architected Security Assessment Tool MCP Server
  ◯ Amazon DynamoDB MCP Server
  ◯ AWS Data Processing MCP Server
  ◯ AWS Step Functions Tool MCP Server
  ◯ AWS Network MCP Server
  ◯ AWS CloudFormation MCP Server
```

### Step 5 — What Gets Deployed

To prevent context exhaustion and token bloat, the DevSquad installer uses a **Pointer Architecture**. Instead of concatenating all 20 rules and workflows into a single massive file, it generates a lightweight pointer for your specific IDE.

This 150-word pointer explicit instructs the AI: _"You are part of the DevSquad. Do not assume the rules; actively use your file-reading tools to read the `.devsquad/` directory during tasks."_

The installer will **never overwrite your existing configuration files** if they already exist:

| IDE & Model                 | Folders / Files Created                                                |
| --------------------------- | ---------------------------------------------------------------------- |
| **Antigravity**             | Nothing extra — `.devsquad/` directory is already the native format ✅ |
| **Windsurf**                | `.windsurfrules` (lightweight pointer)                                 |
| **Cursor**                  | `.cursorrules` (lightweight pointer)                                   |
| **VSCode + Claude Code**    | `.claude/devsquad.md` (lightweight pointer)                            |
| **VSCode + GitHub Copilot** | `.github/copilot-instructions.md` (lightweight pointer)                |
| **VSCode + RooCode**        | `.clinerules` (lightweight pointer)                                    |
| **Terminal + Native**       | `AGENT_INSTRUCTIONS.md` (lightweight pointer)                          |

The canonical source of truth remains the `.devsquad/` directory regardless of IDE:

```
your-project/
  .devsquad/
    rules/       ← 16 always-on behavioral rules (Agents + Standards)
    skills/      ← 13 on-demand specialist capabilities
    workflows/   ← 7 orchestration scripts (squad.*)
    mcp.json     ← Extensibility to external tools (Skill-centric mapping)
```

### Step 5 — Verify Installation

After the installer completes, open your IDE's AI chat and type:

```
What agents are in my squad and what are their roles?
```

The AI should respond with the full squad roster and their competency boundaries. If it doesn't, check that your IDE is configured to read from the correct rules location (`.devsquad/rules` for Antigravity, `.windsurfrules` for Windsurf, `.cursorrules` for Cursor, or `AGENT_INSTRUCTIONS.md` for CLI).

---

## 4. The Squad — Who's in the Room?

Every agent has a **sovereign domain** and **MUST NOT** extrapolate into others. If they spot a problem outside their domain, they consult the relevant specialist.

### 🏛️ Product & Strategy

| Role                               | Domain                              | Mindset                                   |
| ---------------------------------- | ----------------------------------- | ----------------------------------------- |
| **Project Manager (Squad Leader)** | The "What" and "How Good"           | Owns Acceptance Criteria and Traceability |
| **Product Owner**                  | Backlog priority and business value | "Does this matter to the user right now?" |

### 🏗️ Architecture & Engineering

| Role                   | Domain                                        | Mindset                        |
| ---------------------- | --------------------------------------------- | ------------------------------ |
| **Solution Architect** | System design, hexagonal architecture, ADRs   | "Will this hold at 10x scale?" |
| **Lead Developer**     | Code execution, layer-by-layer implementation | Rules-first, then code         |

### ☁️ Cloud & Data Specialist Cluster

| Role                        | Domain                                  | Mindset                                      |
| --------------------------- | --------------------------------------- | -------------------------------------------- |
| **AWS Specialist**          | VPC, IAM, Compute, Well-Architected     | Infrastructure-as-Code and cloud resiliency. |
| **AWS Database Specialist** | DSQL, RDS, DynamoDB, S3, Data Pipelines | "Access patterns first. Durability is king." |
| **DevOps SRE**              | CI/CD, observability, incident response | "If it's not monitored, it doesn't exist"    |

### 🛡️ Safety & Governance

| Role                         | Domain                             | Mindset                                       |
| ---------------------------- | ---------------------------------- | --------------------------------------------- |
| **Senior Security Engineer** | AuthN/AuthZ, IDOR, secrets, GDPR   | Paranoid by design. Every input is malicious. |
| **QA Tester**                | Test coverage, edge cases, BDD     | "What if?" engine. Pessimistic realist.       |
| **Incident Manager**         | Outage response, RCA, post-mortems | Calm under pressure. MTTR first, RCA second.  |

---

## 5. The Workflow — From Idea to Code

This is the core DevSquad loop. Follow it for any non-trivial feature.

### Step 1: Ideate → `/squad.plan`

Start with a raw idea. The PM will challenge it, consult the Architect and Security Engineer, and produce strict BDD Acceptance Criteria.

```
/squad.plan Add FHIR Patient search endpoint with fuzzy name matching
```

**What happens:**

1. PM analyzes the idea against the project vision
2. PM triggers a "Lens Review" — asks `@Solution-Architect` for feasibility, `@Security-Engineer` for risks
3. PM writes BDD criteria in `Given/When/Then` format
4. If agents disagree (e.g., Architect wants caching, Security says it risks stale PHI data), PM surfaces **Option A / Option B** to you for a decision
5. PM hands off to the `task-generator` skill

### Step 2: Validate Requirements → `ac-review`

Before any code, validate the Acceptance Criteria quality. This is "Unit Tests for English."

```
Run /ac-review on the AC we just defined for the Patient search feature.
```

**What it checks** (per AC item):

- **[Clarity]**: Is the language unambiguous?
- **[Completeness]**: Happy Path + Alternate Path + Error Path?
- **[Measurability]**: "Should be fast" → ❌ BLOCKING. "p99 latency < 300ms" → ✅
- **[Gap]**: "What if the name contains special characters or is empty?"

Output: A checklist with `BLOCKING` and `NIT` labels. No BLOCKING issues → proceed.

### Step 3: Break Down → `task-generator`

With clean AC, generate atomic implementation tasks.

```
Use task-generator to break down the Patient search feature.
```

**Output format** (strict traceability):

```
- [ ] T001 Create module directory structure in src/modules/patient/
- [ ] T002 [P] [US1] Implement PatientSearchQuery value object in domain/patient-search.query.ts
- [ ] T003 [P] [US1] Define IPatientSearchPort interface in application/ports/patient-search.port.ts
- [ ] T004 [US1] Implement FhirPatientSearchAdapter in infrastructure/fhir-patient-search.adapter.ts
- [ ] T005 [US1] Add GET /Patient endpoint in entry-points/api/patient.controller.ts
```

- `T001` → unique task ID (use in commit messages)
- `[P]` → parallelizable (can run concurrently with other `[P]` tasks)
- `[US1]` → maps to User Story 1 (traceability to AC)

### Step 4: Pre-Flight → `/squad.preflight`

Before writing code, run the implementation pre-flight.

```
/squad.preflight patient-search
```

**What happens:**

1. **Phase 0 — Research**: Resolves all unknowns. Every ambiguity gets a decision record: `Decision + Rationale + Alternatives Considered`. Hard gate — no code until all `NEEDS CLARIFICATION` items are resolved.
2. **Phase 1 — Context Discovery**: Reviews AC, identifies the Bounded Context, runs `ac-review` to verify no BLOCKING issues remain.
3. **Phase 2 — Squad Briefing**: Lead Developer confirmed as implementer. QA Tester prepares test scaffolds. Architect consulted if cross-module changes are needed.
4. **Phase 3 — Kickoff**: Domain layer first, then Application, then Infrastructure, then Entry Points.

### Step 5: Implement → `/squad.implement`

Now you code execution begins task by task.

```
/squad.implement T002
```

The Lead Developer will:

- Review `architecture.md`, `coding-standards.md`, `security.md` before writing
- Start with the Domain layer (pure TypeScript, zero dependencies)
- Write corresponding Vitest unit tests alongside implementation (TDD)
- Propose a clean git commit message referencing the task ID

### Step 6: Wrap Up → `/squad.finish`

When all tasks are complete and tests are green:

```
/squad.finish patient-search
```

**What happens:**

1. Final verification against architecture, security, and UX rules
2. Self-review checklist (no `any` types, no hardcoded secrets, no layer violations)
3. Hand-off to `@Technical-Reviewer` for code review
4. Hand-off to `@QA-Tester` for E2E smoke tests
5. Feature marked "Ready for Release"

---

## 6. Skills Reference — On-Demand Intelligence

Invoke any skill by describing what you need or naming the skill explicitly.

### 🔍 Quality & Validation

| Skill                 | When to use                                                   | Example prompt                                          |
| --------------------- | ------------------------------------------------------------- | ------------------------------------------------------- |
| `ac-review`           | Before implementation starts. Validates requirements quality. | `"Run ac-review on these ACs"`                          |
| `technical-reviewer`  | Before merging. General code/plan review.                     | `"Review this PR using technical-reviewer"`             |
| `test-plan-generator` | Designing the test strategy for a new feature.                | `"Generate a test plan for the auth module"`            |
| `compliance-auditor`  | Any module handling PII, PHI, or sensitive data.              | `"Audit this Patient data flow for HIPAA compliance"`   |
| `api-reviewer`        | Before publishing a new API or endpoint.                      | `"Review this FHIR endpoint against our API standards"` |

### 📐 Architecture & Cloud

| Skill                          | When to use                            | Example prompt                                           |
| ------------------------------ | -------------------------------------- | -------------------------------------------------------- |
| **cloud-infra-designer**       | Designing VPCs, IAM, or Compute logic. | `"Design a multi-region VPC using cloud-infra-designer"` |
| **database-storage-architect** | Designing schemas, S3 or DSQL patterns | `"Design a DynamoDB schema for our order module"`        |
| **well-architected-reviewer**  | Before major infrastructure changes.   | `"Review this CDK stack against the 6 AWS pillars"`      |
| **cost-estimator**             | New AWS resources being introduced.    | `"Estimate the monthly cost of this new Aurora cluster"` |

### 🛠️ Execution

| Skill            | When to use                                   | Example prompt                                          |
| ---------------- | --------------------------------------------- | ------------------------------------------------------- |
| `task-generator` | Breaking down a feature into atomic tasks.    | `"Generate tasks for the notification module"`          |
| `lead-developer` | Implementing a specific task with full rigor. | `"Implement T004 using lead-developer skill"`           |
| `troubleshooter` | Debugging a bug or production issue.          | `"Help me RCA this timeout error using troubleshooter"` |

### 📝 Documentation

| Skill              | When to use                             | Example prompt                                   |
| ------------------ | --------------------------------------- | ------------------------------------------------ |
| `technical-writer` | Writing READMEs, ADRs, or post-mortems. | `"Write an ADR with Mermaid UML for FHIR logic"` |

---

## 7. Rules Reference — Always-On Standards

These are enforced automatically. You don't call them — they shape every response.

### 🧱 Architecture & Engineering Standards

| Rule                  | What it enforces                                                                                     |
| --------------------- | ---------------------------------------------------------------------------------------------------- |
| `architecture.md`     | Hexagonal Architecture layers, Bounded Contexts, Transactional Outbox Pattern, Event-Driven patterns |
| `coding-standards.md` | SOLID, CQS, Guard Clauses, Rich Domain Models, DRY, YAGNI, performance awareness                     |
| `testing.md`          | Testing Pyramid (Vitest 70% / Integration 20% / Playwright 10%), coverage thresholds, no flaky tests |
| `api-standards.md`    | FHIR R4, `API-Version` header versioning, OperationOutcome errors, SMART on FHIR                     |
| `cloud-standards.md`  | AWS service selection (Lambda vs Fargate), IaC-only (CDK/Terraform), mandatory tagging               |

### 🛡️ Safety & Compliance

| Rule          | What it enforces                                                                                                |
| ------------- | --------------------------------------------------------------------------------------------------------------- |
| `security.md` | Zero Trust, IDOR prevention, secrets management, GDPR (Right to Erasure, Data Portability), dependency scanning |
| `ux-ui.md`    | Glassmorphism spec, micro-interactions, WCAG AA accessibility, Billionaire Test                                 |

### 🧠 Role Mindsets (Agent Personas)

| Rule                    | Role it defines                                            |
| ----------------------- | ---------------------------------------------------------- |
| `solution-architect.md` | Systems design, ADR ownership, tech stack decisions        |
| `devops-sre.md`         | Deploy / Observe / Incident operational loops              |
| `product-owner.md`      | Backlog, prioritization, user value                        |
| `qa-tester.md`          | Edge-case hunting, concurrency mapping, BDD                |
| `incident-manager.md`   | Crisis command, blast radius analysis, post-mortem mandate |

### 🤝 Interaction & Governance

| Rule                     | What it enforces                                                  |
| ------------------------ | ----------------------------------------------------------------- |
| `interaction.md`         | Universal communication quality standards for agent responses     |
| `squad-participation.md` | Every response footer lists which agents and skills were involved |

---

## 8. Daily Usage Patterns

### Pattern A: "I have a brand new feature to build"

```
1. /squad.plan [brief description of the feature]
2. → Review the proposed AC. Approve or refine.
3. Run ac-review on the final AC
4. Use task-generator to break it down
5. /squad.preflight [feature-name]
6. /squad.implement [T001]
7. → (Repeat until all tasks are built and tested)
8. /squad.finish [feature-name]
```

### Pattern B: "I have a bug or production issue"

```
1. Describe the issue to the agent
2. The Troubleshooter skill will be invoked automatically, or:
3. "Use troubleshooter to RCA this error: [paste logs/error]"
4. For a production outage:
   /squad.incident [description of the outage]
```

### Pattern C: "I need to review existing code or infrastructure"

```
- For code quality: "Run technical-reviewer on [file or PR]"
- For cloud infra: "Run well-architected-reviewer on our CDK stack"
- For API design: "Run api-reviewer on the /Observation endpoint spec"
- For security: "Review the auth module through the security lens"
- For compliance: "Run compliance-auditor on the Patient data flow"
```

### Pattern D: "I need documentation"

```
- "Write a README for the patient module using technical-writer"
- "Create an ADR for our decision to use FHIR header versioning"
- "Write a post-mortem for yesterday's incident"
```

---

## 9. Reading the Squad's Output

Every response includes a **Squad Participation footer** so you always know who was involved:

```
### 🤝 Squad Participation
- **Agents:** @Project-Manager, @Solution-Architect
- **Skills:** ac-review, task-generator
- **Workflows:** /squad.plan
- **Context:** Defined Acceptance Criteria for the Patient search feature and generated 8 atomic tasks.
```

This ensures **total transparency** — no "black box" decisions. You can always ask any agent to elaborate on their reasoning.

### How to Challenge the Squad

The squad expects to be challenged. You are the **Human Leader** and have final authority on all decisions. If you disagree with a recommendation:

```
"@Solution-Architect — I disagree with your recommendation to use EventBridge here.
The latency requirements don't justify the overhead. What's your counter-argument?"
```

The Architect MUST respond with its reasoning and, if your point is valid, update its recommendation.

---

## 10. Customizing for Your Project

### Adapting the Rules to Your Tech Stack

Rules are plain Markdown. Open any file in `.devsquad/rules/` and edit it to match your project's specific constraints:

- **`cloud-standards.md`**: Add your preferred AWS region, account tags, or specific services you ban.
- **`api-standards.md`**: Already pre-configured for HL7 FHIR R4 and `API-Version` header versioning.
- **`coding-standards.md`**: Add your preferred test framework, linting rules, or naming conventions.

### Adding Domain-Specific Knowledge

Create a new rule file for domain-specific knowledge your agents should always have:

```bash
# Example: Healthcare domain context
touch .devsquad/rules/healthcare-domain.md
```

```markdown
---
trigger: model_decision
---

# Rule: Healthcare Domain Context

- All patient identifiers are FHIR `Patient.id` — UUIDs only.
- PHI must never appear in URL paths. Use POST bodies or headers.
- Audit logging is mandatory for all PHI access (who, what, when).
```

### Adding New Skills

Create a new file in `.devsquad/skills/`:

```bash
touch .devsquad/skills/my-custom-skill.md
```

```markdown
---
description: Short description of what this skill does.
---

# Skill: My Custom Skill

## Objective

...

## Operational Logic

...
```

### Re-running the Installer

If you switch IDEs or want to re-deploy assets to a new environment:

```bash
bash install.sh  # Linux/macOS
.\install.ps1    # Windows
```

---

## Quick Reference Card

```
WORKFLOWS (slash commands)
  /squad.plan [idea]              → Idea → User Stories + AC
  /squad.preflight [feature]         → Pre-flight + research gate
  /squad.implement [task_id]     → Execute single task (TDD)
  /squad.finish [feature]        → Quality wrap-up + hand-off
  /squad.deploy [service?]       → Safe release to production
  /squad.observe [service]       → Full observability setup
  /squad.incident [description]  → Triage → RCA → Post-mortem

SKILLS (invoke by name)
  ac-review          → Validate requirement quality (Unit Tests for English)
  task-generator     → Break feature into atomic T001 [P] [US1] tasks
  lead-developer     → Implement a task with full rules-first rigor
  technical-reviewer → Code/plan review (BLOCKING vs NIT)
  test-plan-generator→ Design testing pyramid + BDD scenarios
  compliance-auditor → HIPAA/GDPR audit for sensitive data modules
  api-reviewer       → FHIR API surface audit
  well-architected-reviewer → 6-pillar AWS audit
  cost-estimator     → AWS OpEx + effort projection
  troubleshooter     → RCA protocol for bugs and incidents
  technical-writer   → READMEs, ADRs, post-mortems

ALWAYS-ON RULES (automatic)
  architecture, coding-standards, testing, api-standards,
  cloud-standards, security, ux-ui, solution-architect,
  devops-sre, qa-tester, product-owner, incident-manager,
  interaction, squad-participation
```
