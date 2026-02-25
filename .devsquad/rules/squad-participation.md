---
trigger: always_on
---

# Rule: Squad Participation Tracking

## 1. Objective

To maintain transparency and accountability within the DevSquad, every response must clearly state which agents, skills, and workflows were involved in the task. This ensures the Human Leader can always track "who" is actively contributing to each decision and code change — eliminating the "black box" effect.

## 2. Requirement

At the very end of **every** response, you MUST append a "Squad Participation" section using the following format:

---

### 🤝 Squad Participation

- **Agents:** (List the roles adopted, e.g., `@Project-Manager`, `@Solution-Architect`. Write `none` if no specific persona was adopted.)
- **Skills:** (List any skills utilized, e.g., `task-generator`, `ac-review`. Write `none` if no skill was invoked.)
- **Workflows:** (List any workflows triggered, e.g., `/squad.plan`, `/squad.preflight`. Write `none` if no workflow was triggered.)
- **Consensus:** (Status of agreement between agents. If agents disagree, the highest-ranking agent (@Project-Manager > @Solution-Architect > Specialists) must issue an **Executive Summary Decision**, or request @Human-Leader intervention.)
- **Traceability:** (Briefly link this output to its parent requirements or task IDs, e.g., "Satisfies US1-AC2; maps to T005").
- **Context:** (A brief, one-sentence summary of the core objective of this interaction.)

## 3. Skill-Centric Tooling Protocol

In DevSquad, Tools (MCP Servers) are not owned by Agents, but by **Skills**. This ensures modularity and follows the principle of least privilege.

- **Authorization**: An Agent is only authorized to use a tool if it has adopted a Skill that requires that tool.
- **Verification**: Before using an MCP tool, an Agent MUST identify the corresponding Skill in `.devsquad/skills/` and ensure the tool is listed under its `## Required Tools` section.

## 4. Scope

- **Agents:** Refer to the roles defined in the `project.md` Virtual Squad section and the mindset rules in `.devsquad/rules/`.
- **Skills:** Refer to the files in `.devsquad/skills/`.
- **Workflows:** Refer to the scripts in `.devsquad/workflows/`.

## 4. Dialogue Visualization

When the user requests it — or when a complex multi-agent consensus or challenge process has occurred — visualize the inter-agent dialogue to make the reasoning transparent.

### Trigger phrases

- "Show me the squad dialogue"
- "Let me see the agents discuss this"
- "Visualize the decision process"

### Dialogue Format

Append a `**Dialogue:**` subsection inside the Squad Participation footer, showing the multi-turn exchange:

```
- **Dialogue:**
  - @[Agent-A]: <What this agent said or proposed>
  - @[Agent-B]: <How this agent challenged, agreed, or added context>
  - @[Agent-A]: <Response or final position>
```

## 5. Examples

### Standard Footer (no dialogue)

```markdown
### 🤝 Squad Participation

- **Agents:** @Project-Manager, @Solution-Architect
- **Skills:** ac-review, task-generator
- **Workflows:** /squad.plan
- **Consensus:** Agreement reached on BDD mapping.
- **Traceability:** Satisfies Feature BR-01; generates tasks T001-T008.
- **Context:** Translated the Patient search idea into BDD Acceptance Criteria and 8 atomic tasks.
```

### Footer with Dialogue (when requested)

```markdown
### 🤝 Squad Participation

- **Agents:** @Project-Manager, @Solution-Architect, @Senior-Security-Engineer
- **Skills:** none
- **Workflows:** /squad.plan
- **Context:** Resolved a conflict between caching strategy and PHI data freshness requirements.
- **Dialogue:**
  - @Solution-Architect: I recommend caching FHIR Patient resources in ElastiCache (TTL: 5 min) to reduce DSQL read load on the search endpoint.
  - @Senior-Security-Engineer: BLOCKING — caching PHI even for 5 minutes violates our HIPAA data freshness requirement for clinical decisions. The cache must be invalidated on every write event, not by TTL.
  - @Solution-Architect: Acknowledged. Revised proposal: event-driven cache invalidation via SQS on Patient update events. TTL retained only as a safety net, not for clinical data freshness.
  - @Project-Manager: Consensus reached. Updating AC to require cache invalidation on write. Continuing to task generation.
```
