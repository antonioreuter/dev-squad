# Implementation Plan: DevSquad Specialized Expansion

This plan outlines the steps to pivot DevSquad to a **Skill-Centric Tooling** architecture, introduce specialized AWS/Database agents, and enhance collaboration through critical challenge protocols.

## Phase 1: Standardizing the Brain (The "Tool-to-Skill" Pivot)

Goal: Ensure tools are assigned to Skills, not Agents, for modularity and least-privilege.

- [ ] **P1-T1: Update Agent Mindsets**. Remove direct `## MCP Tools` sections from existing `.devsquad/rules/*.md` files (Solution Architect, DevOps SRE, etc.).
- [ ] **P1-T2: Reassign Tools to Skills**. Update `.devsquad/skills/*.md` files to include a `## Required Tools` section.
- [ ] **P1-T3: Update Execution Rules**. Update `.devsquad/rules/squad-participation.md` to define the protocol: Agents derive their tool authorization from the active Skill.

## Phase 2: Defining the Specialist Cluster (AWS & DB)

Goal: Introduce deep AWS and Database expertise with Well-Architected alignment.

- [ ] **P2-T1: Create AWS Specialist Agent**. Define residency in `rules/aws-specialist.md`. Focus: Infrastructure design, Well-Architected Framework.
- [ ] **P2-T2: Create AWS Database Specialist Agent**. Define residency in `rules/aws-database-specialist.md`. Focus: DB patterns, S3/Storage, Performance.
- [ ] **P2-T3: Create Specialist Skills**.
  - `skills/cloud-infrastructure-designer.md` (General AWS VPC/Networking/IAM).
  - `skills/database-storage-architect.md` (DSQL, S3, RDS, DynamoDB).
- [ ] **P2-T4: Map specialized tools**. Assign AWS Pricing, Well-Architected Tool, and Data Processing MCPs to these skills.

## Phase 3: Enhancing Planning & Collaboration

Goal: Add Mermaid.js support and strengthen "Critical Thinking" mandates.

- [ ] **P3-T1: Enrich Planner & Writer**. Update existing skills to include Mermaid.js UML generation instructions (Sequence, Class, State diagrams).
- [ ] **P3-T2: Strengthen Challenge Protocol**. Update `.devsquad/rules/interaction.md` to mandate a "Devil's Advocate" check in every multi-agent discussion.
- [ ] **P3-T3: Implement /squad-help update**. Reflect new roles and skills in the central help command.

## Phase 4: Operationalizing the Framework (CLI & Docs)

Goal: Synchronize documentation and improve the developer experience.

- [ ] **P4-T1: Audit & Gap Analysis**. Review `project.md` for consistency gaps between the new vision and existing specs.
- [ ] **P4-T2: Update project.md**. Reflect the new specialized agents in the "Virtual Squad" section.
- [ ] **P4-T3: Update CLI Installer**. Modify `dev_squad/cli.py` to prompt for MCP configuration and explain tool-to-skill mapping.
- [ ] **P4-T4: Full Tutorial Overhaul**. Update `TUTORIAL.md` with sections on MCP tools, Mermaid.js diagrams, and the Specialist Cluster.

---

### 🤝 Squad Participation

- **Agents:** @Solution-Architect
- **Skills:** task-generator
- **Workflows:** none
- **Context:** Organized the project expansion into a 4-phase implementation plan following the "Tool-to-Skill" architecture.
