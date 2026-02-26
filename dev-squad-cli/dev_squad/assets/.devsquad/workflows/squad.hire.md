# Workflow: /squad.hire [Name] [Description] [Tools]

**Trigger:** `/squad.hire [Name] "[Role Description]" "[Tool list]"`
**Category:** HR Workflow
**Authority:** `@HR-Manager` only.

## 1. Purpose

To expand the squad's capabilities by onboarding new specialists or re-activating archived ones.

## 2. Steps

### Step 1: Identification

- Check `.devsquad/fired/` for a matching `[Name]` (Re-hiring a customized specialist).
- If not found, check `.devsquad/_addons/` for a matching pack (Hiring from the global pool).
- If still not found, research industry-standard competencies for the role and draft the initial `.md` assets (Rule, Skill) to match the squad's architectural standards.
- Prepare the "Employment Contract" including the origin (Fired/Add-on/New).

### Step 2: Tool Pre-flight

- Identify any MCP tools in `[Tool list]`.
- Check if tools are already in `mcp.json` or system path.
- **CRITICAL**: Detect host environment (IDE/Agent) and prepare installation commands (`npm install`, `pip install`).

### Step 3: Employment Contract

Present the following to the `@Human-Leader`:

- **Role Summary**: [Name] - [Description].
- **Permission Scope**: Assigned rules and tools.
- **Resource Cost**: New MCP servers to be added.
- **Setup Plan**: Installation steps for required libraries.

### Step 4: Execution (Wait for "Approved")

- Deploy/Restore assets to `.devsquad/rules/`, `.devsquad/skills/`, etc.
- Execute tool installations.
- Update `.devsquad/mcp.json` with new configurations.
- **Social-Aware Sync**:
  - Add the new specialist to `.devsquad/devsquad-settings.json` with `status: active`.
  - **Template Deployment**:
    - Copy global templates from `.devsquad/templates/` to the project if not present.
    - If hiring from an addon, copy `templates/` from the addon directory to the active project.
  - **Social Update**: Iterate through existing active agents and add the new hire to their `collaborates` list if applicable.
- Update `project.md` active squad table.

## 3. Definition of Done

- Assets are live in standard paths.
- MCP tools are installed and configured.
- `devsquad-settings.json` is updated with the new agent and **new peer links established** in the collaboration lists of existing squad members.
- `project.md` updated with Name, Description, and Active status.
