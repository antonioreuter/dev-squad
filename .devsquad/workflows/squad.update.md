---
description: Updates the local DevSquad environment with the latest core assets while preserving project configurations.
---

# Workflow: /squad.update

**Trigger:** `/squad.update`
**Category:** Maintenance Workflow
**Authority:** `@HR-Manager` or `@Project-Manager`.

## 1. Purpose

To synchronize the local `.devsquad` environment with the latest core rules, skills, and workflows from the DevSquad source, while preserving project-specific configurations like `devsquad-settings.json` and `mcp.json`.

## 2. Steps

### Step 1: Pre-flight Check

- Verify the existence of the `.devsquad/` directory.
- Confirm the current environment (CLI/IDE).

### Step 2: Execution

- Instruct the user (or execute directly if authorized) the following command:
  ```bash
  dev-squad update
  ```
- **Note**: This command performs a surgical update:
  - **Refreshed**: `rules/`, `skills/`, `workflows/`, `templates/`.
  - **Preserved**: `devsquad-settings.json`, `mcp.json`.

### Step 3: Verification

- Confirm that the core assets have been refreshed by checking file timestamps or versions.
- Ensure the squad registry (`devsquad-settings.json`) is still intact and reflects the current active agents.

## 3. Definition of Done

- Latest core logic is deployed to the project.
- No local configuration settings were overwritten.
- Multi-agent collaboration remains operational with newest protocols.
