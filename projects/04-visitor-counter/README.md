# Project 04 — Real-Time Visitor Counter

## Overview
A real-time visitor counter embedded in the resume website, incrementing on every page visit using a serverless backend and DynamoDB atomic counters.

## Live Demo
[https://d2wwi6wx69tjrn.cloudfront.net](https://d2wwi6wx69tjrn.cloudfront.net)

## Services Used
- **Lambda** — Counter increment function
- **DynamoDB** — visitor-counter table with atomic updates
- **API Gateway** — REST API endpoint

## Architecture
```
Page Load → API Gateway → Lambda → DynamoDB (atomic increment) → Return count
```

## Key Concepts Demonstrated
- DynamoDB atomic counter pattern
- Lambda function with DynamoDB SDK calls
- CORS configuration on API Gateway
- Real-time data display on frontend
