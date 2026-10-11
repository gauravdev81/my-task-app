# Task Management API

## Purpose
REST API for creating, updating, deleting and retrieving tasks.

## Tech Stack
Python
FastAPI
Pydantic
SQLAlchemy
Psycopg
PostgreSQL

## Architecture

Client
 ↓
FastAPI
 ↓
Pydantic
 ↓
Service layer
 ↓
SQLAlchemy
 ↓
Psycopg
 ↓
PostgreSQL

## Database
Users
Tasks

## APIs
POST /tasks
GET /tasks
GET /tasks/{id}
PUT /tasks/{id}
DELETE /tasks/{id}

## Authentication
...

## Error Handling
...

## Environment Configuration
...

## Problems I faced
...

## Important decisions
...