---
description: Audits cloud designs against the 6 Pillars of the AWS Well-Architected Framework.
---

# Skill: Well-Architected Reviewer

## 1. Objective

Ensures cloud infrastructure is built according to AWS best practices for sustainability, security, and performance.

## 2. The 6 Pillars Audit

- **Operational Excellence**: Is there enough monitoring/logging? Can we recover from failure?
- **Security**: Is IAM least-privileged? Is data encrypted at rest/transit?
- **Reliability**: Is it multi-AZ? Is there a backup strategy?
- **Performance Efficiency**: Are we over-provisioned? Is the compute choice optimal?
- **Cost Optimization**: Are we using Serverless where possible? Any idle resources?
- **Sustainability**: Minimizing the environmental impact of compute and storage.

## 3. Operational Logic

1. Scan the `cloud-standards.md` compliance.
2. Review CDK/Terraform code if available.
3. Identify "High Risk Issues" (HRIs) and propose remediation.
