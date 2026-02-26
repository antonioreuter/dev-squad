---
description: Safely removes an employee from the active squad while preserving their specialized knowledge for potential re-hiring.
---

# Workflow: /squad.fire [EmployeeName]

**Trigger:** `/squad.fire [EmployeeName]`
**Category:** HR Workflow
**Authority:** `@HR-Manager` only.

## 1. Purpose

To safely remove an employee from the active squad while preserving their specialized knowledge for potential re-hiring.

## 2. Steps

### Step 1: Inventory & Dependency Check

- Identify all assets linked to `[EmployeeName]` in `.devsquad/` (rules, skills, workflows).
- **CRITICAL**: Search the entire codebase for references to these files using `grep`.
- Identify any shared rules or skills that would be broken by this dismissal.

### Step 2: Dismissal Proposal

Present the following to the `@Human-Leader`:

- **Reason**: Brief justification for the dismissal.
- **Asset List**: Files to be moved.
- **Impact Assessment**: Note any shared dependencies that will be retained or renamed.
- **MCP Status**: List of MCP servers that will be deactivated.

### Step 3: Execution (Wait for "Approved")

- Move files to `.devsquad/fired/[EmployeeName]/`.
- Update environment-specific ignore files (detected by `@hr-specialist`).
- Disable entries in `.devsquad/mcp.json`.
- **Social-Aware Cleanup**:
  - Remove the agent from `.devsquad/devsquad-settings.json`.
  - **Template Decommissioning**:
    - Identify templates specific to this agent (from their origin addon) and remove them from the active project.
    - Move agent-specific templates to `.devsquad/fired/[EmployeeName]/templates/`.
  - **Social Purge**: Iterate through all remaining active agents and remove the dismissed agent from their `collaborates` list.
- **Registry Sync**: Move agent from `active_agents` to `graveyard` in `.devsquad/devsquad-settings.json`.

## 3. Definition of Done

- Files are isolated in `fired/` subfolders.
- Ignore files updated.
- `devsquad-settings.json` is updated and **all peer collaboration lists cleaned**.
- `devsquad-settings.json` reflects the change.
- `mcp.json` is cleaned.
