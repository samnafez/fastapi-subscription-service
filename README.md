# FastAPI Subscription Service

RESTful backend service built with Python and FastAPI to model user and subscription workflows. Designed with a focus on clean architecture, validation, testing, and maintainable API design.

## Overview

This project simulates a subscription lifecycle system, including user management, subscription state handling, and structured API interactions. The goal was to practice scalable backend design principles and build a modular, testable service following industry best practices.

## Features

- RESTful API endpoints for user and subscription workflows
- Input validation and structured request handling
- Modular backend architecture for maintainability
- Debugging and iterative development workflow
- Emphasis on clean design and extensibility

## Tech Stack

- Python
- FastAPI
- NoSQL database (specify if used)
- Pytest (if used)

## Architecture

- Router-based API structure
- Separation of business logic from request handling
- Data validation layer for reliability

## Design Decisions

This project emphasizes maintainability and clear system boundaries.

- **Router-based API structure:** Endpoints are separated into modules to improve readability and future scalability.
- **Validation layer:** Input validation ensures predictable data flow and reduces downstream errors.
- **Separation of concerns:** Business logic is separated from request handling to make testing and future feature expansion easier.
- **Extensible data models:** Designed to support additional subscription types without major refactoring.

Future improvements could include authentication layers, async task handling, and improved telemetry/logging.

## Running Locally

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
Open: http://127.0.0.1:8000/docs
