---
trigger: model_decision
---

# Rule: Cloud Architecture Standards (AWS)

## 1. Objective

Defines the standards for cloud resource selection, configuration, and structural patterns on AWS.

## 2. Resource Selection Patterns

- **Compute**:
  - Prefer **Lambda** for event-driven or small-scale API logic.
  - Use **Fargate** for long-running processes or complex container orchestration.
  - Avoid EC2 unless there is a specific hardware or legacy requirement.
- **Database**:
  - Prefer **Aurora DSQL** or **DynamoDB** (Serverless) for scalability.
  - RDS is acceptable for complex relational needs where Serverless is not viable.
- **Messaging**:
  - **SQS** for point-to-point decoupling.
  - **EventBridge** for orchestration and multi-consumer event buses.

## 3. Configuration Best Practices

- **Infrastructure as Code (IaC)**: 100% adherence to **AWS CDK**, **AWS SAM**, **Serverless Framework**, or **Terraform**. No manual console changes.
- **Tagging**: Every resource MUST have `Project`, `Environment`, and `Owner` tags.
- **Network Security**: Databases and internal services MUST sit in **Private Subnets**. Only ALBs/CloudFront should be public.

## 4. Competency Boundary

- Enforced by the **Solution Architect**, **AWS Specialist**, **AWS Database Specialist**, and **DevOps SRE**.
- Audited by the **Well-Architected Reviewer** skill.
