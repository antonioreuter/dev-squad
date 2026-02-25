# DevSquad: Agentic Spec-Driven Development Platform

## 1. Vision & Executive Summary

**DevSquad** is an autonomous, collaborative AI orchestration framework designed to revolutionize the software development lifecycle (SDLC) through **Spec-Driven Development (SDD)**. Unlike traditional automation, DevSquad treats AI agents as a multidisciplinary "Virtual Squad," where specialized personas collaborate, challenge each other, and iterate on complex problems in real-time.

By applying **Systems Thinking**, DevSquad moves beyond linear task execution to a feedback-rich ecosystem where specifications are the single source of truth, and agents act as both creators and gatekeepers of quality, security, and compliance.

---

## 2. Systemic Architecture

The DevSquad system is built on four pillars:

1.  **Elements**: Specialized AI Agents with distinct cognitive roles.
2.  **Interconnections**: Collaborative workflows and inter-agent communication protocols.
3.  **Purpose**: The agile delivery of high-quality, production-ready systems.
4.  **Feedback Loops**: Continuous review cycles (e.g., Security, QA, and Compliance auditing) that ensure the system evolves and corrects itself during the development process.

---

## 3. The Virtual Squad (Roles)

Agents are organized into "Clusters" to ensure structural integrity and clear accountability:

### A. Product & Strategy Cluster

- **Project Manager (PM)**: The **Squad Leader**. Defines the vision, orchestrates the workflow, and ensures technical execution aligns with strategic goals.
- **Product Owner (PO)**: Manages the backlog and ensures the team delivers business value.
- **UX/UI Designer**: Responsible for creating the user interface and user experience, ensuring visual consistency and usability align with requirements.
- **Domain Expert**: Provides deep industry context (e.g., Fintech, Healthtech). _Note: Configurable per-project._

### B. Architecture & Engineering Cluster

- **Solution Architect**: Designs the system backbone, ensuring scalability and hexagonal patterns. **Competency**: Systems high-level design, ADRs, and tech stack decisions.
- **Lead Developer**: Oversees implementation patterns and technical consistency. **Competency**: Code quality, design patterns, and task execution.
- **Senior Software Engineer**: Executes high-complexity coding tasks and component design. **Competency**: Individual module implementation and refactoring.
- **DevOps SRE**: Responsible for infrastructure as code, deployment pipelines, and observability. **Competency**: AWS infrastructure, CI/CD, and performance monitoring.

### C. Safety & Governance Cluster

- **Senior Security Engineer**: The "Paranoid Guardrail." Performs threat modeling and enforces "Security by Design." **Competency**: Auth/Auth patterns, vulnerability scanning, and compliance isolation.
- **Compliance Auditor**: Validates adherence to regulatory standards (HIPAA, GDPR, etc.). **Competency**: Regulatory alignment and PII protection.
- **QA Tester**: Defines and executes testing strategies (Unit, Integration, E2E). **Competency**: Test coverage, edge-case detection, and bug reports.
- **Incident Manager**: Handles troubleshooting and manages the resolution of production-level issues. **Competency**: Root cause analysis and service restoration.

---

## 4. Capabilities & Infrastructure

To empower the Squad, agents are equipped with specialized "Skills" and "Tools."

### Specialized Skills

- **Estimation & Review**: `cost-estimator`, `well-architected-reviewer`, `technical-reviewer`, `api-reviewer`.
- **Documentation**: `technical-writer`.
- **Validation & Safety**: `compliance-auditor` (HIPAA/GDPR), `test-plan-generator`, `ac-review`.
- **Execution**: `task-generator`, `lead-developer`, `troubleshooter`.

### Integrated Tools

- **Cloud Native**: MCP (Model Context Protocol) servers for AWS integration.
- **Custom Tooling**: Extensible toolsets for DB management, API exploration, and repository analysis.

---

## 5. Collaborative Workstreams (Boards)

DevSquad operates through standardized **Boards** that synchronize multiple agents toward specific milestones. While these boards provide a structured path, the framework remains **non-prescriptive**—users have the freedom to engage agents individually or bypass board structures entirely.

### Board 1: Design & Requirements Hardening (DRH)

- **Focus**: Requirements integrity and architectural validation.
- **Activities**: Gap analysis in High-Level Designs (HLD), AWS Well-Architected reviews, API verification, and Risk/DFMEA estimation. Agents are mandated to **challenge the PM's specifications**—if AC is vague or technically unfeasible, the Solution Architect or QA Tester must flag it and propose refinements.

### Board 2: Strategic Planning & Decomposition

- **Focus**: Translating vision into actionable units.
- **Activities**: Feature breakdown into granular **Use Cases**, definition of **Acceptance Criteria (AC)** at both feature and task levels.

### Board 3: Autonomous Implementation

- **Focus**: High-fidelity execution and verification.
- **Activities**: Requirement-to-task translation, code implementation, and automated generation of the "Test Pyramid" (Unit, Integration, Security, and E2E).

### Board 4: Quality Assurance (QA) & Validation

- **Focus**: Final acceptance and compliance.
- **Activities**: Validating implemented code against recursively defined **Acceptance Criteria (AC)**. Every task must satisfy its specific AC, which in turn rolls up to satisfy the high-level Feature AC. This ensures intrinsic traceability without redundant matrices.

---

## 6. Governance & Collaboration Protocols

To ensure harmony in a multi-agent environment, DevSquad follows strict interaction rules:

- **Sovereign Domains & Competency Boundaries**: Each agent is the sovereign authority of its domain but **MUST NOT** extrapolate competency into others. This is enforced through modular mindset rules (`solution-architect.md`, `qa-tester.md`, `devops-sre.md`, `product-owner.md`). If an agent identifies a problem outside its domain, it must **Consult** the relevant specialist rather than attempting a fix.
- **Strategic Critical Thinking**: Agents are mandated to exercise independent judgment. If they identify ambiguity, strategic gaps, or a better approach _within their domain_, they **MUST** challenge the current plan. When challenging, they must present **viable options** to the Human Leader, explicitly stating their recommended course of action and the "Why."
- **Consensus through Peer Challenge**: DevSquad operates on a "Devil's Advocate" protocol. Agents are not passive recipients of specs; they are expected to critique and challenge each other's outputs. If the **Solution Architect** finds the **PM's** Acceptance Criteria vague, they must request clarification. consensus is reached when agents agree on a technical path, or when the **Human Leader** breaks a deadlock.
- **State Synchronization**: The Squad maintains a **Global Context** through a shared project ledger. This ensures that an agent entering at Board 4 (QA) has full visibility into the strategic decisions and risks identified in Board 1 (DRH), preventing context drift.
- **Secret Integrity**: Security is non-negotiable. All MCP tool credentials and API keys must be managed via encrypted environment variables or secure vault integrations; hardcoding secrets in configuration files is strictly prohibited.
- **Dynamic Peer Support**: Agents are inherently collaborative and will autonomously request help from other specialists (e.g., a Lead Dev requesting a Security review) when thresholds are met.
- **Total Transparency**: Every "behind-the-scenes" communication between agents is logged and visible, preventing the "black box" effect.
- **Decision Logging**: Every request concludes with a **Squad Execution Summary**, documenting:
  - **Participants**: Which agents were involved.
  - **Consensus**: Key technical or product decisions made.
  - **Traceability**: Links between requirements, implementation, and tests.
- **Standards**: Strict adherence to AWS Architecture, Security-by-Design, and Clean Code principles.

---

## 7. Strategic Differentiation: DevSquad vs. GitHub SpecKit

While inspired by [GitHub SpecKit](https://github.com/github/spec-kit), DevSquad introduces critical evolutions:

1.  **Flexibility over Rigidity**: Where SpecKit is template-heavy and restrictive (e.g., branch-per-spec), DevSquad is adaptive. Developers can refine specs, start implementation from ideas, or call agents directly as needed.
2.  **Collaborative Intelligence**: DevSquad is built on _collaboration_ (Agent-to-Agent) rather than just _generation_ (Agent-to-File).
3.  **End-to-End Lifecycle**: DevSquad doesn't just write specs; it generates tasks based on Acceptance Criteria, implements code, and audits against those criteria.

---

## 8. Reference Implementation: The "Source Agent" Model

A tangible prototype of this framework is available in the `source-agent/` directory, specifically optimized for the **Antigravity IDE**. This reference implementation serves as a blueprint for how the Virtual Squad is configured and orchestrated.

### Core Structure

The reference project demonstrates a modular "Agent Assets" architecture:

- **`.devsquad/rules/`**: Modular constraints — `architecture.md`, `coding-standards.md`, `security.md`, `ux-ui.md`, `testing.md`, `cloud-standards.md`, `api-standards.md`, `incident-manager.md` + role mindsets.
- **`.devsquad/skills/`**: `task-generator`, `lead-developer`, `cost-estimator`, `well-architected-reviewer`, `technical-writer`, `technical-reviewer`, `troubleshooter`, `api-reviewer`, `compliance-auditor`, `test-plan-generator`.
- **`.devsquad/workflows/`**: `/pm-spec`, `/start-implementation`, `/finish-implementation`.
- **`mcp.json`**: Pre-configured integration with external services (GitHub, Linear, AWS, Figma, Playwright).

### Key Workflow Highlight: The PM Orchestrator

The reference implementation features a **PM Orchestrator** workflow. As the Squad Leader, the PM mediates between requirements and execution, ensuring that implementation (starting from a spec or just an idea) always satisfies the Acceptance Criteria.

---

## 9. Ecosystem Agnosticism & Distribution

DevSquad is designed to function as a "Universal Brain" that adapts to its host environment. It respects the unique particularities of different tools, OSs, and models.

### A. The installer "Wizard" (Agnostic Bridge)

Instead of a persistent agent workflow, DevSquad utilizes a one-time **Installer Wizard** (e.g., `install.sh` or `setup.js`). This wizard acts as the distribution bridge:

- **Environment Detection**: Probes for the OS (Linux/macOS/Windows) and the active IDE environment.
- **Smart Distribution**: Copies and adapts core assets (Rules, Skills, Workflows) into the specific paths and formats required by the target IDE (e.g., `.cursorrules` for Cursor, `.windsurfrules` for Windsurf).
- **Model Optimization**: Prompts the user for their preferred model provider and injects the corresponding prompt-engineering particularities into the system configuration.

### B. Cross-Platform "Environmental Adapter"

The installer and runtime handle OS-specific particularities:

- **OS Support**: Native installers for **Linux (Debian/RPM/Arch)**, **macOS (Homebrew/Silicon)**, and **Windows (WSL2/PowerShell)**.
- **Shell Awareness**: Automatically detects and configures required paths for `zsh`, `bash`, and `powershell`.
- **Dependency Management**: Handles installation of required runtimes (Node.js, Python, Go) and MCP host binaries per OS architecture.

---

## 10. Agnostic Orchestration (Models & Providers)

DevSquad does not favor a single LLM. Instead, it utilizes **Model-Tiering** based on the task's cognitive requirements:

- **Reasoning Tier (Planning & Design)**: Optimized for models like **Claude 3.7 Sonnet**, **GPT-4o**, or **Gemini 1.5 Pro**. Used for Board 1 (DRH) and Board 4 (QA).
- **Execution Tier (Coding & Tasks)**: Optimized for fast, tool-capable models like **Claude 3.5 Haiku** or **GPT-4o-mini**.
- **Model-Specific Prompting**: The orchestration layer dynamically adjusts prompt structures (e.g., System Message placement, XML tags vs. JSON blocks) to respect the "particularities" of the provider's API (Anthropic, OpenAI, AWS Bedrock, Google Vertex).

---

## 11. Roadmap & Evolution

- [x] Universal "Bridge Layer" for IDE Asset Translation (Installer Wizard).
- [x] Strategy for "Sovereign Domains" & "Competency Boundaries".
- [x] Initial Modular Mindset Rules (PM, Architect, Security, UX, QA, SRE, PO).
- [ ] Multi-Model Provider Support (Automatic Prompt Optimization - Deferred for Zen).
- [ ] MCP AWS Toolset & Ecosystem Integration.
- [ ] Multi-IDE Plugin Marketplace.
