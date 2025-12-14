# Project Proposal – Serverless Notes API

## Team Roster
- **Sai Vardhan Meesala**
- **Sai Krishna Praneeth Talari**

## Problem & Goal
We are building a basic serverless notes API on AWS. Users can create and retrieve text-based notes through `POST /notes` and `GET /notes`. The goal is to demonstrate cloud-native design, managed services, observability, and deployment practices.

## User Flow
1. User sends `POST /notes` with `title` and `body`.
2. API Gateway forwards request to Lambda.
3. Lambda writes a new item to DynamoDB.
4. User sends `GET /notes`.
5. Lambda retrieves and returns all notes.

## Chosen Compute + Data
- **Compute:** AWS Lambda + API Gateway HTTP API  
- **Data:** Amazon DynamoDB (NoSQL)

## Architecture (Rough)
Client → API Gateway → Lambda → DynamoDB

## Initial SLO & Monitoring Plan
- **Availability SLO:** 99% successful (2xx) responses per month.
- **Monitoring:** CloudWatch (Lambda errors, throttles, logs)

## Initial Team Roles
Both members share design, coding, deployment, monitoring, and documentation.  
Final roles will be split as:
- Infrastructure (Terraform/Monitoring): Sai Vardhan  
- Lambda API code + docs: Sai Krishna  
