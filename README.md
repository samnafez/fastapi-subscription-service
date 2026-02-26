# FastAPI Subscription Service

RESTful backend service built with Python and FastAPI to model user and subscription workflows. Designed with a focus on clean architecture, validation, testing, and maintainable API design.

## Overview

This project simulates a subscription lifecycle system, including user management, subscription state handling, and structured API interactions. The goal was to practice scalable backend design principles and build a modular, testable service following industry best practices.

## Features

- RESTful API endpoints for user and subscription workflows
- Input validation using Pydantic schemas
- Modular router-based API structure
- SQLAlchemy ORM integration for database interactions
- Structured separation of business logic from request handling
- Iterative debugging and refinement workflow

## Tech Stack

- Python
- FastAPI
- SQLAlchemy (ORM)
- SQLite (local development database)
- Uvicorn

## Architecture

- Router-based API structure (`app/routers/`)
- ORM models defined in `models.py`
- Pydantic schemas for request/response validation
- Centralized database session management
- Clear separation of concerns between API layer and data layer

## Design Decisions

This project emphasizes maintainability and clear system boundaries.

- **Router-based API structure:** Endpoints are separated into modules to improve readability and scalability.
- **Validation layer:** Pydantic schemas ensure predictable data flow and reduce downstream errors.
- **Separation of concerns:** Business logic is separated from request handling to support easier testing and feature expansion.
- **Extensible data models:** Designed to support additional subscription types without major refactoring.

## Project Structure

- `app/main.py` — FastAPI application entrypoint  
- `app/routers/` — API route modules  
- `app/models.py` — SQLAlchemy ORM models  
- `app/schemas.py` — Pydantic schemas  
- `app/database.py` — Database engine and session configuration  

## Future Improvements

- Authentication and authorization layer  
- Asynchronous task handling  
- Improved telemetry and structured logging  
- Expanded automated test coverage  

## Running Locally

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
