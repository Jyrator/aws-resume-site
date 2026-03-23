# Project 12 — Containers with ECS and Fargate

## Overview
A fully serverless containerised web application deployed on AWS Fargate via Amazon ECS. Docker image built locally, pushed to ECR, and served via an Application Load Balancer — zero EC2 instances.

## Services Used
- **Docker** — Container image build
- **Amazon ECR** — ejiro-container-app (private image registry)
- **Amazon ECS** — ejiro-ecs-cluster (container orchestration)
- **AWS Fargate** — Serverless container runtime
- **Application Load Balancer** — ejiro-ecs-alb
- **CloudWatch Logs** — /ecs/ejiro-container-app
- **IAM** — ecsTaskExecutionRole
- **VPC** — Multi-AZ across us-east-1a and us-east-1b

## Architecture
```
Internet → ALB (ejiro-ecs-alb) → ECS Fargate Tasks (×2)
                                          ↑
                                    ECR (Docker Image)
                                          ↓
                                   CloudWatch Logs
```

## Key Concepts Demonstrated
- Docker containerisation and ECR image management
- ECS task definitions and service configuration
- Fargate serverless compute (no EC2 required)
- ALB target group with IP address target type
- Centralised container logging via CloudWatch
