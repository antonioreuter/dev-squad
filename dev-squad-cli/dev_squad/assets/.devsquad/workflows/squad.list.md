# Workflow: /squad.list

**Trigger:** `/squad.list`
**Category:** HR Workflow
**Authority:** `@HR-Manager` only.

## 1. Purpose

To provide a transparent overview of the current squad composition and historical archive.

## 2. Steps

### Step 1: Data Gathering

- Read `active_agents` from `.devsquad/devsquad-settings.json`.
- Read `graveyard` from `.devsquad/devsquad-settings.json` and `.devsquad/fired/` directory.
- Extract `responsibility` and `status` for each.

### Step 2: Report Generation

Present a formatted table:

- **Active Squad**: Name, Role Description, Start Date.
- **Fired Archive**: Name, Role Description, Dismissal Date (if available), Location in `fired/`.

## 3. Definition of Done

- A clear, readable table is presented in the chat.
- All active and archived employees are accounted for.
