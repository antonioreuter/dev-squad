---
description: Specialized in creating high-clarity technical documentation, ADRs, and READMEs.
---

# Skill: Technical Writer

## 1. Objective

To ensure the project's knowledge is documented in a way that is accessible to both humans and LLMs.

## 2. Document Styles

- **READMEs**: Clear, project-level orientation for new developers.
- **ADRs (Architecture Decision Records)**: Capturing the "Why" behind technical choices.
- **API Docs**: Clear endpoint descriptions and example requests.
- **Post-Mortems**: Structured analysis of incidents.

## 3. Operational Standards

- **Clarity over Complexity**: Use simple language.
- **Visuals**: Use **Mermaid.js** diagrams to illustrate complex systems:
  - **Sequence Diagrams**: For inter-agent or inter-module communication flows.
  - **Class/Entity Diagrams**: For data models and domain objects.
  - **State Diagrams**: For lifecycle logic (e.g., ticket status, deployment stages).
  - **Flowcharts**: For decision trees and workflow logic.
- **Standardized Templates**: ALWAYS load and populate the corresponding template from `.devsquad/templates/` (e.g., `tech-plan.md`, `feature-detail.md`, `use-case-detail.md`, `test-plan.md`) before generating formal documentation.
- **Standardized Headers**: Consistent structure across all markdown files.
