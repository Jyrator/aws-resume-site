# Project 08 — Custom VPC Network Architecture

## Overview
A production-style custom VPC built from scratch with public and private subnets across multiple Availability Zones, Internet Gateway, NAT Gateway, route tables, and security groups.

## Services Used
- **VPC** — ejiro-vpc (10.0.0.0/16)
- **Subnets** — Public (10.0.1.0/24, 10.0.3.0/24) and Private (10.0.2.0/24)
- **Internet Gateway** — ejiro-igw
- **NAT Gateway** — Private subnet internet access
- **Route Tables** — ejiro-public-rt, ejiro-private-rt
- **Security Groups** — ejiro-public-sg, ejiro-private-sg

## Architecture
```
Internet → IGW → Public Subnet (Web Tier)
                      ↓ NAT GW
                 Private Subnet (DB Tier)
```

## Key Concepts Demonstrated
- VPC design with public/private subnet separation
- NAT Gateway for private subnet outbound access
- Route table configuration
- Security group layering (web tier vs DB tier)

## Architecture Diagram

