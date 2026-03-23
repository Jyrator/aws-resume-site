# Project 11 — Auto Scaling Group with Application Load Balancer

## Overview
A fault-tolerant, self-healing web application deployed across multiple Availability Zones using an Application Load Balancer and Auto Scaling Group. Demonstrated live CPU stress testing and automatic scale-out.

## Services Used
- **EC2** — t3.micro, Amazon Linux 2023, Apache
- **Application Load Balancer** — ejiro-alb
- **Auto Scaling Group** — ejiro-asg (Desired: 2, Min: 2, Max: 4)
- **Launch Template** — ejiro-asg-template
- **CloudWatch** — CPU alarms (scale out >70%, scale in <30%)
- **VPC** — Multi-AZ across us-east-1a and us-east-1b

## Architecture
```
Internet → ALB (ejiro-alb) → ASG (2-4 x EC2 t3.micro)
                                        ↕
                               CloudWatch Alarms
```

## Key Concepts Demonstrated
- High availability across multiple AZs
- Target tracking scaling policy
- ALB health checks and traffic distribution
- Self-healing infrastructure (ASG replaces failed instances)
- IMDSv2-compliant EC2 metadata access
