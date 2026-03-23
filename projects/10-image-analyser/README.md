# Project 10 — AI Image Analyser with Rekognition

## Overview
An AI-powered image analysis tool that detects objects, scenes, and labels in uploaded images using Amazon Rekognition, with results displayed in real time.

## Live Demo
[https://d3ipadtt6x7vlf.cloudfront.net/rekognition.html](https://d3ipadtt6x7vlf.cloudfront.net/rekognition.html)

## Services Used
- **Rekognition** — AI image analysis and label detection
- **Lambda** — rekognition-function
- **S3** — ejiro-rekognition-images (temporary image storage)
- **API Gateway** — rekognition-api endpoint
- **CloudFront** — Frontend delivery

## Architecture
```
User uploads image → API Gateway → Lambda → S3 (store) → Rekognition (analyse) → Return labels
```

## Key Concepts Demonstrated
- Amazon Rekognition label detection API
- S3 temporary object storage pattern
- Multi-step Lambda orchestration
- AI/ML service integration without model training

## Architecture Diagram

