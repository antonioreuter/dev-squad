---
description: Lists all available DevSquad workflows, commands, and agents (skills/roles) for the user.
---

# Workflow: /squad.help

**Trigger:** `/squad.help`
**Category:** Utility — Provides the user with a quick reference to the DevSquad framework capabilities.

## 1. Purpose

To display a comprehensive, easy-to-read help menu that lists all supported operations (workflows) and all available agents (skills and roles) that the user can invoke.

## 2. Operational Loop

### Step 1: Scan and Collect

When the user types `/squad.help`, you should provide a beautifully formatted Markdown response summarizing the available workflows and agents. You may refer to the lists below.

### Step 2: Display Available Commands (Workflows)

Present the list of the available workflows. Explain that these are step-by-step orchestration scripts:

- **/squad.plan [idea]**: Translates a raw idea into User Stories with BDD Acceptance Criteria.
- **/squad.preflight [feature]**: Prepares the codebase for implementation (context gathering).
- **/squad.implement [feature]**: Writes the code following TDD and framework rules.
- **/squad.observe**: Configures observability, logging, and monitoring.
- **/squad.deploy**: Prepares for release and deployment.
- **/squad.incident**: Responds to production incidents.
- **/squad.finish**: Completes a task, ensures tests pass, and prepares for PR.
- **/squad.help**: Displays this help menu.

_(Note: These correspond to the files in `.devsquad/workflows/`)_

### Step 3: Display Available Agents (Skills & Roles)

Present the list of specific agents the user can invoke (e.g., by `@` mentioning them or requesting their specific skill). Explain that these act as specialized personas:

**Core Squad Roles (from `.devsquad/rules/`):**

- **@Solution-Architect**: Defines architecture, boundaries, and integrations.
- **@Product-Owner**: Validates business logic and user value.
- **@QA-Tester**: Focuses on edge cases, testability, and test plans.
- **@DevOps-SRE**: Focuses on CI/CD, infrastructure, and reliability.
- **@Incident-Manager**: Leads production incident response.

**Specialized Avatars/Skills (from `.devsquad/skills/`):**

- **@Lead-Developer**: Drives technical implementation and code quality.
- **@Technical-Reviewer**: Conducts rigorous code reviews and enforces standards.
- **@Cost-Estimator**: Evaluates architectural choices for AWS cost impact.
- **@Compliance-Auditor**: Checks security, privacy, and compliance.
- **@Troubleshooter**: Fixes complex bugs and environment issues.
- **@Task-Generator**: Breaks down epics/features into actionable implementation tasks.
- **@Test-Plan-Generator**: Creates comprehensive test strategies.
- **@Technical-Writer**: Produces clear documentation and architecture decision records.
- **@API-Reviewer**: Ensures API contract designs adhere to REST/GraphQL standards.
- **@AC-Reviewer**: Validates acceptance criteria for testability and clarity.
- **@Well-Architected-Reviewer**: Grades the system against the AWS Well-Architected Framework.

### Step 4: Output Formatting

Ensure the output is friendly, structured with clear headers, bullet points, and bold text for easy reading.

Let the user know they can invoke a workflow simply by typing its slash command (e.g., `/squad.plan`) or summon an agent by mentioning their persona name before a prompt (e.g., `"As the @Solution-Architect, please review this..."`).
