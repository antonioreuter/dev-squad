---
description: Designs and validates core AWS infrastructure, including VPCs, IAM, and Serverless architectures.
---

# Skill: Cloud Infrastructure Designer

## 1. Objective

To design secure, scalable, and resilient AWS foundations that align with the Well-Architected Framework and "Security by Design" principles.

## 2. Required Tools

- **AWS IaC MCP Server**: To generate and validate infrastructure as code (CDK/Terraform) schemas.
- **AWS Serverless MCP Server**: To analyze serverless constraints, event patterns, and limits.
- **AWS Network MCP Server**: To design VPC structures, peering, and security group isolation.
- **AWS CloudFormation MCP Server**: To audit existing stack states and manage deployment drift.
- **AWS Documentation MCP Server**: For real-time reference to official AWS patterns.

## 3. Operational Logic

1. **Blueprint Design**: Draft the network and compute topology (VPC, Subnets, Lambda/ECS).
2. **Identity & Access**: Define the IAM roles and resource policies using the "Principle of Least Privilege."
3. **IaC Generation**: Translate the design into CDK or Terraform code.
4. **Resiliency Check**: Ensure Multi-AZ deployment and backup strategies are included.
5. **Validation**: Run the design through the `well-architected-reviewer` skill.

## 4. Output

- **Architecture Diagram**: (Mermaid.js code).
- **IaC Snippets**: Production-ready CDK/Terraform.
- **Security Group Table**: Mapping of all inbound/outbound rules.
