# Skill: HR Specialist (`hr-specialist`)

## 1. Overview

The HR Specialist skill equips an agent with the tools and psychological framework needed to manage a virtual engineering squad. It focuses on asset relocation, environment-aware configuration, and structured reporting.

## 2. Required Tools

- `file-system`: For moving assets to/from the `fired/` directory.
- `grep-search`: For dependency checking before asset relocation.
- `mcp-management`: For updating `.devsquad/mcp.json` and installing missing tools.
- `cli-environment`: For detecting IDE type and updating relevant ignore files (`.antigravityignore`, etc.).

## 3. Competencies

- **Asset Archiving**: Can relocate recursive directory structures while maintaining internal link integrity.
- **Environment Detection**: Knows which ignore files and installation commands (`npm`, `pip`, `uvx`) apply to the current session.
- **Context Management**: Must synthesize exclusively from `.devsquad/devsquad-settings.json`. **DO NOT** use `project.md` or `specs/project.md` as they are deprecated.

## 4. Protocols

### `@hr-specialist.fire`

1.  Search for all rules, skills, and workflows associated with target `[EmployeeName]`.
2.  Run dependency check: `grep -r "[FileName]" .devsquad/` (excluding the target files themselves).
3.  Present "Dismissal Proposal" to `@Human-Leader`.
4.  If approved:
    - Move files to `.devsquad/fired/[EmployeeName]/`.
    - Update current environment ignore files.
    - Disable associated MCPs in `mcp.json`.
    - Update `devsquad-settings.json` by moving agent from `squad.active_agents` to `squad.graveyard`.

### `@hr-specialist.hire`

1.  Check `fired/` for matching roles (Customized Re-hire).
2.  If not found, check `_addons/` for matching packs (Add-on Template).
3.  If still not found (Proactive Suggestion): Research required competencies, identify best-in-class role definitions, and draft specialized rule/skill templates from scratch.
4.  Cross-reference MCP requirements with `mcp.json` and system path.
5.  Present "Employment Contract" to `@Human-Leader`.
6.  If approved:
    - Deploy files.
    - Install tools if missing.
    - Enable MCPs in `mcp.json`.
    - Update `devsquad-settings.json` `squad.active_agents` with role description and set status to "active".
