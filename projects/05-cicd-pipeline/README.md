# Project 05 — CI/CD Pipeline with GitHub Actions

## Overview
An automated deployment pipeline that pushes updates to S3 and invalidates the CloudFront cache on every commit to the main branch.

## Services Used
- **GitHub Actions** — CI/CD workflow automation
- **S3** — Deployment target
- **CloudFront** — Cache invalidation on deploy
- **IAM** — github-actions-user with least-privilege permissions

## Workflow
```
git push → GitHub Actions → AWS CLI sync to S3 → CloudFront invalidation
```

## Key Concepts Demonstrated
- CI/CD pipeline automation
- IAM least-privilege access for deployment user
- GitHub Actions secrets management
- CloudFront cache invalidation strategy

## Workflow File
`.github/workflows/deploy.yml`

## Architecture Diagram

