# API Design – Serverless Notes API

This document defines the API contract for our AWS-based serverless notes application.  
The API has two routes:

- `POST /notes` – Create a new note (WRITE)
- `GET /notes` – Retrieve all notes (READ)

---

## 1. POST /notes

### Description
Creates a new note with a title and body. The backend generates a unique `note_id` and timestamps the entry.

### Request
**Method:** POST  
**Path:** `/notes`  
**Content-Type:** `application/json`

### Request Body Example
```json
{
  "title": "Shopping List",
  "body": "Milk, Eggs, Bread"
}
