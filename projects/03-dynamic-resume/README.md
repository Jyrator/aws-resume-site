# Project 03 — Dynamic Resume with Admin Panel

## Overview
A dynamic resume that pulls content from DynamoDB, with a password-protected admin panel for updating resume content without touching code.

## Live Demo
[https://d2wwi6wx69tjrn.cloudfront.net](https://d2wwi6wx69tjrn.cloudfront.net)

## Services Used
- **S3** — Frontend hosting
- **CloudFront** — CDN and HTTPS
- **Lambda** — Resume data retrieval and admin functions
- **DynamoDB** — Resume content storage (ejiro-resume table)
- **API Gateway** — REST API

## Architecture
```
User → CloudFront → S3 (Frontend)
Frontend → API Gateway → Lambda → DynamoDB
Admin Panel → API Gateway → Lambda → DynamoDB (write)
```

## Key Concepts Demonstrated
- DynamoDB as a NoSQL content store
- Serverless CRUD operations via Lambda
- Password-protected admin functionality
- Dynamic content rendering from API responses

## Architecture Diagram

