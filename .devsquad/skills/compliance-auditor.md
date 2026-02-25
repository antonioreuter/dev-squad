---
description: On-demand audit for HIPAA and GDPR compliance when handling sensitive user data.
---

# Skill: Compliance Auditor (HIPAA/GDPR)

## 1. Objective

Ensures that all modules involving PII (Personally Identifiable Information) or PHI (Protected Health Information) adhere to strict legal and privacy standards.

## 2. Required Tools

- **AWS Well-Architected Security Assessment Tool MCP Server**: For automated compliance and security posture checks.

## 3. PII/PHI Audit Checklist

- **Encryption**: Is data encrypted in transit (TLS 1.2+) and at rest (AES-256)?
- **Access Control**: Is access logged and restricted to "Need-to-know"?
- **Data Minimization**: Are we collecting only the absolute minimum data required?
- **Masking**: Is sensitive data masked or hashed in application logs?

## 3. Operational Logic

1. **Trigger**: This skill should be invoked whenever a feature involves `User`, `Health`, `Identity`, or `Billing` modules.
2. **Audit Output**: A checklist of compliance risks found and mandatory remediation steps.
3. **Traceability**: Link findings to specific regulatory requirements (e.g., GDPR Article 25).
