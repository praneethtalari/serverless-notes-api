# Serverless Notes API – Cloud Computing Final Project

## Team Members
- **Sai Vardhan Meesala**
- **Sai Krishna Praneeth Talari**

## Project Overview
This project implements a fully serverless Notes API on AWS. Users can create and retrieve short text notes using an HTTP interface. The system demonstrates cloud-native architecture, serverless compute, DynamoDB NoSQL design, monitoring with CloudWatch, IAM least-privilege, and Infrastructure as Code using Terraform.  
An optional S3-hosted UI is also included.

## Repo Structure
- `/app` – Lambda function code (Python)
- `/infra` – Infrastructure as Code (Terraform for Lambda, API Gateway, DynamoDB, IAM, CloudWatch)
- `/docs` – Proposal, architecture diagram, API design, DynamoDB schema, collaboration plan, SLO/monitoring
- `/project` – Final narrative report + screenshots for submission

## Features
- POST /notes → Create a note
- GET /notes → Retrieve all notes
- DynamoDB table for storage
- AWS Lambda for compute
- API Gateway HTTP API for routing
- CloudWatch Logs + Alarms
- Terraform IaC deployment

## Deployment (Terraform)
Inside `/infra`:

```
terraform init
terraform validate
terraform plan
terraform apply
```

Outputs:
- API base URL
- /notes endpoint

## Testing
Create a note:
```
curl -X POST "<API_URL>/notes" \
  -H "Content-Type: application/json" \
  -d '{ "title": "Hello", "body": "From UI" }'
```

Get all notes:
```
curl "<API_URL>/notes"
```

## Architecture Diagram
Included in `/docs`:
- architecture_diagram.drawio
- architecture_diagram.svg
- architecture_diagram.png (optional)

## Monitoring & SLOs
- Availability SLO: 99% successful API requests
- Latency SLO: p95 < 200ms
- CloudWatch alarms for Lambda errors, API 5xx, DynamoDB throttles

## Project Phase Status
- Phase 0 – Repository setup ✔
- Phase 1 – API design & DynamoDB schema ✔
- Phase 2 – Lambda development ✔
- Phase 3 – Terraform automation ✔
- Phase 4 – SLO / Monitoring plan ✔
- Phase 5 – Architecture diagram ✔
- Phase 6 – Testing / Validation ✔
- Phase 7 – Final writeup & documentation ✔

## Deliverables Included
- Proposal  
- API design  
- DynamoDB schema  
- Collaboration plan  
- SLO & Monitoring plan  
- Architecture diagram  
- Final report  
- Screenshots  

## Summary
This project successfully implements a cloud-native, serverless Notes API using AWS managed services and Terraform. It meets all professor requirements and demonstrates proper architecture, observability, deployment practices, and documentation.
