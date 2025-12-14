# SLO & Monitoring Plan – Serverless Notes API

This document defines Service Level Objectives (SLOs) and the monitoring strategy for the AWS-based Serverless Notes API.

The goal is to ensure reliability, detect issues, and tie observability directly to our application flows (`POST /notes` and `GET /notes`).

---

# 1. Service Level Objectives (SLOs)

## 1.1 Availability SLO
**SLO:**  
At least **99% of all requests** to `/notes` (POST and GET) must return a **2xx status code** over a 30-day window.

**Why:**  
Ensures users can reliably create and retrieve notes.

---

## 1.2 Latency SLO
**SLO:**  
- p95 latency for **POST /notes** < **400 ms**  
- p95 latency for **GET /notes** < **300 ms**

**Why:**  
Lambda + DynamoDB should normally respond fast; this keeps the app responsive.

---

## 1.3 Error Rate SLO
**SLO:**  
- 5xx errors must remain **below 2%** over any rolling 5-minute interval.

**Why:**  
Server errors indicate issues with Lambda, IAM, or DynamoDB.

---

# 2. Monitoring Plan (AWS CloudWatch)

We will monitor system reliability using Amazon CloudWatch metrics + logs.

---

# 2.1 Metrics to Monitor

### Lambda Function Metrics
| Metric | Reason |
|--------|--------|
| **Errors** | Detect Lambda failures |
| **Invocations** | Traffic levels |
| **Duration** | Detect slowdowns affecting latency SLO |
| **Throttles** | Should always be 0; affects reliability |

---

### API Gateway Metrics
| Metric | Reason |
|--------|--------|
| **4xxError** | Bad client requests |
| **5xxError** | Upstream Lambda failures |
| **Latency** | Must meet p95 latency SLO |

---

### DynamoDB Metrics
| Metric | Reason |
|--------|--------|
| **ThrottledRequests** | Provisioned capacity issues |
| **SuccessfulRequestLatency** | Important for overall performance |

---

# 2.2 Logs

### Lambda CloudWatch Logs
- Request payloads (optional logging)
- Error stack traces  
- Useful for debugging failures and validating the SLO plan.

---

# 3. Alerting Plan (Design-Level)

Even if alerts are not implemented, we define what we *would* alert on:

---

## Alert #1 — API 5xx Errors Too High
**Trigger:** `5xxError > 2%` for 5 minutes  
**Why:** Violates availability + error SLO  

---

## Alert #2 — High Lambda Error Count
**Trigger:** `Errors > 5` in 5 minutes  
**Why:** Indicates Lambda failures or bad IAM permissions  

---

## Alert #3 — DynamoDB Throttling
**Trigger:** `ThrottledRequests > 0`  
**Why:** Should never happen; indicates misconfiguration  

---

## Alert #4 — High Latency
**Trigger:** `p95 > 400 ms` over 5 minutes  
**Why:** Violates latency SLO  

---

# 4. Optional (Enhancement Feature): Implemented Monitoring Alarms

(To be filled in if created)

If implemented via AWS console or Terraform, include:
- CloudWatch Alarm name(s)
- Associated metric(s)
- SNS topic for notifications

---

# 5. Summary

This SLO & Monitoring plan is directly tied to our app’s core flows:
- Creating notes (`POST /notes`)
- Retrieving notes (`GET /notes`)

The design follows industry best practices:
- Latency, availability, and error SLOs
- Metrics at Lambda, API Gateway, and DynamoDB layers
- Simple alerting rules mapped to real failure modes
