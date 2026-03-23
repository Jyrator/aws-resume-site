# Project 02 — Serverless AI Chatbot

## Overview
A serverless AI chatbot powered by Amazon Bedrock (Nova Micro model), accessible via a static frontend hosted on S3 and CloudFront.

## Live Demo
[https://d3ipadtt6x7vlf.cloudfront.net](https://d3ipadtt6x7vlf.cloudfront.net)

## Services Used
- **Lambda** — Chatbot backend function
- **Amazon Bedrock** — Nova Micro foundation model
- **API Gateway** — REST API endpoint
- **S3** — Static frontend hosting
- **CloudFront** — Global CDN

## Architecture
```
User → CloudFront → S3 (Frontend)
User → API Gateway → Lambda → Bedrock (Nova Micro)
```

## Key Concepts Demonstrated
- Serverless architecture with zero EC2 instances
- Amazon Bedrock foundation model invocation
- API Gateway Lambda proxy integration
- S3 static website hosting with CloudFront

## Architecture Diagram

