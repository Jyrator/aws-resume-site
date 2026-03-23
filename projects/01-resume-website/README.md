# Project 01 — Resume Website on EC2

## Overview
A personal resume website hosted on an Apache web server running on Amazon EC2, served globally via CloudFront.

## Live Demo
[https://d2wwi6wx69tjrn.cloudfront.net](https://d2wwi6wx69tjrn.cloudfront.net)

## Services Used
- **EC2** — t3.micro instance running Amazon Linux 2023
- **Apache** — Web server
- **CloudFront** — Global CDN and HTTPS termination
- **Security Groups** — HTTP/HTTPS/SSH access control

## Architecture
```
User → CloudFront → EC2 (Apache) → Resume HTML
```

## Key Concepts Demonstrated
- EC2 instance launch and configuration
- Apache web server setup via user data
- CloudFront distribution with custom origin
- Security group rules for web traffic
