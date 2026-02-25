---
description: Estimates the implementation effort and the potential AWS cloud cost of a feature or architecture.
---

# Skill: Cost Estimator

## 1. Objective

To prevent "Economic Surprise" by providing early visibility into both developer effort (complexity) and AWS resource costs.

## 2. Operational Logic

1. **Effort Estimation**:
   - Analyze the `TASK.md` or Implementation Plan.
   - Categorize complexity: Low (1-2 days), Medium (3-5 days), High (5+ days).
2. **Infrastructure Cost (AWS)**:
   - Identify new resources (e.g., RDS Instance, DynamoDB Provisioning, Lambda traffic).
   - Estimate monthly OpEx based on standard AWS pricing tiers.
3. **Optimizations**:
   - Suggest cheaper alternatives if the cost/value ratio is high (e.g., using SQS/Lambda instead of a persistent EC2 queue).

## 3. Output

- **Complexity Score**: (1-10)
- **AWS OpEx Impact**: (Approx. $/month)
- **Efficiency Recommendations**: (List of alternatives)

## 4. MCP Tools

- **AWS Pricing MCP Server**: Retrieve real-time pricing data for precise AWS OpEx calculations.
