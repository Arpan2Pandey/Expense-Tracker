# Expense Tracker API

A backend API built using FastAPI and PostgreSQL to manage personal expenses.

## Features

- Add expenses
- View all expenses
- View all stored expenses
- Delete expenses
- Calculate total spending

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy

## Run Locally

Install dependencies:

pip install -r requirements.txt

Start the server:

uvicorn app.main:app --reload

Open API docs:

http://127.0.0.1:8000/docs