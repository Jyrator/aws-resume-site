# Project 09 — Serverless Contact Form with SES

## Overview
A serverless contact form that sends emails via Amazon SES, embedded in the resume website. No servers, no mail infrastructure — fully managed email delivery.

## Live Demo
[https://d2wwi6wx69tjrn.cloudfront.net](https://d2wwi6wx69tjrn.cloudfront.net)

## Services Used
- **Lambda** — Form processing function
- **SES** — Email delivery (ejirosaks@gmail.com verified)
- **API Gateway** — contact-form-api endpoint

## Architecture
```
Contact Form → API Gateway → Lambda → SES → ejirosaks@gmail.com
```

## Key Concepts Demonstrated
- SES email identity verification
- Lambda form validation and sanitisation
- API Gateway CORS configuration
- Serverless email pipeline

## Architecture Diagram

