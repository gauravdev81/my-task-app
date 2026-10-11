# My Task App

A simple Task Management API built with **FastAPI** and Python.

This project is created for learning and practicing backend API development with FastAPI.

## Features

- Create tasks
- Get tasks
- Update tasks
- Delete tasks
- API request/response validation using Pydantic
- Interactive API documentation with Swagger UI

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## Project Structure

```text
my-task-app/
│
├── src/
│   └── ...
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

## Local Setup

- Create a virtual env. Enter in venv.
- Install FastAPI using `pip install "fastapi[standard]"`
- Install Sqlalchemy using `pip install sqlalchemy` (ORM) and 
- pip install psycopg