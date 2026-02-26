# FastAPI Subscription Service

Production-style REST API built with **FastAPI** modeling a SaaS subscription lifecycle.

This project simulates real-world subscription management including user creation, plan validation, lifecycle transitions (activation/cancellation), and relational persistence using SQLAlchemy.

---

## Overview

This backend service models a simplified subscription platform similar to SaaS products.

The project focuses on:

- Clean architecture
- Predictable state transitions
- Schema-driven validation
- Proper HTTP semantics
- Extensible backend design

---

## Core Features

- RESTful API following resource-based conventions
- User creation and persistence
- Subscription creation with enum-based plan validation (`Basic`, `Standard`, `Premium`)
- Subscription cancellation via partial updates (`PATCH`)
- Structured error handling (400 / 404 / 422)
- SQLAlchemy ORM integration with relational modeling
- Swagger-generated interactive API documentation

---

## Example API Usage

### Create a User

**Request**

```http
POST /users
Content-Type: application/json
```

```json
{
  "email": "user@example.com"
}
```

**Response (200 OK)**

```json
{
  "id": 1,
  "email": "user@example.com"
}
```

---

### Create a Subscription

**Request**

```http
POST /subscriptions
Content-Type: application/json
```

```json
{
  "user_id": 1,
  "plan": "Premium"
}
```

**Response (200 OK)**

```json
{
  "id": 1,
  "user_id": 1,
  "plan": "Premium",
  "active": true
}
```

---

### Invalid Plan (Validation Error)

**Request**

```http
POST /subscriptions
Content-Type: application/json
```

```json
{
  "user_id": 1,
  "plan": "Gold"
}
```

**Response (422 Unprocessable Entity)**

```json
{
  "detail": [
    {
      "loc": ["body", "plan"],
      "msg": "Input should be 'Basic', 'Standard' or 'Premium'",
      "type": "enum"
    }
  ]
}
```

---

### Cancel a Subscription

**Request**

```http
PATCH /subscriptions/1?active=false
```

**Response (200 OK)**

```json
{
  "id": 1,
  "user_id": 1,
  "plan": "Premium",
  "active": false
}
```

---

## Tech Stack

- Python 3
- FastAPI
- SQLAlchemy (ORM)
- SQLite
- Uvicorn
- Pydantic

---

## Architecture

```
app/
├── main.py
├── routers/
├── models.py
├── schemas.py
├── database.py
```

### Design Principles

- Separation of concerns between routing, validation, and persistence
- Schema-first validation using Pydantic
- Controlled subscription lifecycle management
- Extensible backend structure

---

## Future Improvements

- Authentication and role-based access control
- Payment simulation layer
- Docker containerization
- Cloud deployment
- Expanded automated test coverage

---

## Running Locally

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

Open:

http://127.0.0.1:8000/docs
