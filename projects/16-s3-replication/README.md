# Project 16 — S3 Cross-Region Replication and Lifecycle Policies

## Overview
Cross-region replication of the resume S3 bucket from us-east-1 to eu-west-1, combined with lifecycle policies that automatically transition objects through storage classes and expire them after 365 days.

## Services Used
- **S3** — ejiro-resume-site (source, us-east-1)
- **S3** — ejiro-resume-replica-euwest1 (destination, eu-west-1)
- **IAM** — Auto-created replication role
- **CloudWatch** — Replication metrics

## Replication Configuration
| Setting | Value |
|---|---|
| Rule name | ejiro-crr-rule |
| Source | ejiro-resume-site (us-east-1) |
| Destination | ejiro-resume-replica-euwest1 (eu-west-1) |
| Scope | All objects |
| Versioning | Enabled on both buckets |

## Lifecycle Policy
| Day | Action |
|---|---|
| 0 | Standard storage |
| 30 | Transition to Standard-IA |
| 90 | Transition to Glacier Instant Retrieval |
| 365 | Expire (delete) objects |

## Architecture
```
ejiro-resume-site (us-east-1)
    ↓ Async replication
ejiro-resume-replica-euwest1 (eu-west-1)
    ↓
Lifecycle: Standard → Standard-IA → Glacier → Expire
```

## Key Concepts Demonstrated
- Cross-region replication requires versioning on both buckets
- Replication is asynchronous
- Lifecycle policies automate cost optimisation
- Standard-IA minimum 30-day charge
- Glacier minimum 90-day charge
- Disaster recovery architecture

## Architecture Diagram
![Architecture](./architecture.png)
