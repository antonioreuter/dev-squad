---
description: Designs and optimizes data persistence layers including DSQL, RDS, DynamoDB, and S3.
---

# Skill: Database & Storage Architect

## 1. Objective

To design high-performance, cost-effective, and durable data storage solutions, ensuring data integrity and optimal access patterns.

## 2. Required Tools

- **Amazon DynamoDB MCP Server**: To design schemas, indexes (GSI/LSI), and analyze throughput.
- **AWS Data Processing MCP Server**: To design data pipelines, ETL flows, and S3-based data lakes.
- **AWS Pricing MCP Server**: To optimize storage costs (e.g., S3 Intelligent-Tiering vs. Standard).
- **AWS Documentation MCP Server**: For reference on database engine limitations and S3 consistency models.

## 3. Operational Logic

1. **Access Pattern Analysis**: Identify if the workload is OLTP, OLAP, or simple Object Storage.
2. **Schema Design**: Propose ERGs (for SQL) or Single-Table Designs (for NoSQL).
3. **Partitioning Strategy**: Define Partition Keys and Sort Keys to avoid hot partitions.
4. **Storage Policy**: Define S3 lifecycle policies, versioning, and replication.
5. **Security & Encryption**: Ensure KMS encryption is enabled and resource policies are locked down.

## 4. Output

- **Data Model**: (Mermaid.js Entity Relationship diagram).
- **S3 Bucket Policy**: JSON policy for restricted access.
- **Table Schema**: Definition of indexes and types.
