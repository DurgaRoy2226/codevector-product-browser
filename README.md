# CodeVector Product Browser

A backend service built using FastAPI and PostgreSQL for browsing large product catalogs efficiently.

## Features

* Browse products sorted by newest first
* Filter products by category
* Cursor-based pagination
* PostgreSQL database
* FastAPI backend
* Seed script for generating large datasets
* Designed to scale for 200,000+ products

## Tech Stack

* FastAPI
* SQLAlchemy
* PostgreSQL (Neon)
* Faker
* Python

## API Endpoints

### Get Products

GET /products

Optional query parameters:

* category
* cursor_id

Example:

GET /products?category=Books

## Running Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Author

Durga Roy
