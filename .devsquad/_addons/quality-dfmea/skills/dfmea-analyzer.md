# Skill: DFMEA Analyzer (`dfmea-analyzer`)

## 1. Overview

The DFMEA Analyzer skill provides a structured methodology for identifying potential failure modes in a system design, assessing their impact, and defining preventive or corrective mitigations.

## 2. Required Tools

- `grep-search`: To analyze existing designs and cross-reference potential failure points.
- `technical-writer`: To document the DFMEA matrix.

## 3. DFMEA Methodology

For every component in the design, evaluate:

1. **Failure Mode**: What could go wrong? (e.g., "Database connection timeout").
2. **Potential Effect**: What is the impact on the user/system? (e.g., "Data loss during checkout").
3. **Severity (S)**: 1-10 scale of impact.
4. **Potential Cause**: Why would it fail? (e.g., "Network latency", "Incorrect pooling config").
5. **Occurrence (O)**: 1-10 scale of likelihood.
6. **Current Controls**: What prevents this now?
7. **Detection (D)**: 1-10 scale of how easily we find it.
8. **RPN (Risk Priority Number)**: S x O x D.

## 4. Operational Logic

1. **Scan Design**: Read the `implementation_plan.md` or architecture documents.
2. **Brainstorm Failures**: Focus on boundary conditions, integrations, and data persistence.
3. **Mitigation Strategy**: For every HRPN (High RPN) item, propose a concrete architectural or code-level mitigation.
4. **Output**: Generate a `DFMEA_ANALYSIS.md` log for the project.
