# CodeVector Product Browser

This project is a backend product browsing application built as part of the CodeVector assignment. It is developed using **FastAPI**, **SQLAlchemy**, and **PostgreSQL (Neon)**. The application allows users to browse a large product catalog, filter products by category, and navigate through products using **cursor-based pagination**.

The database contains **200,000 products**, allowing the API to be tested with a realistic large dataset.

---

## Live Demo

**Application:**
https://codevector-product-browser-mq05.onrender.com

**API Documentation:**
https://codevector-product-browser-mq05.onrender.com/docs

**Products API:**
https://codevector-product-browser-mq05.onrender.com/products

**Frontend:**
https://codevector-product-browser-mq05.onrender.com/browse

---

## Features

* Browse products sorted by newest first
* Filter products by category
* Cursor-based pagination
* FastAPI REST API
* PostgreSQL (Neon) database
* Simple frontend for browsing products
* Seed script for generating product data
* Tested with a dataset of 200,000 products

---

## Technology Stack

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL (Neon)
* Jinja2
* Faker

---

## API Endpoints

| Method | Endpoint    | Description           |
| ------ | ----------- | --------------------- |
| GET    | `/`         | Health check          |
| GET    | `/products` | Browse products       |
| GET    | `/browse`   | Frontend page         |
| GET    | `/docs`     | Swagger documentation |

### Query Parameters

| Parameter | Description                                 |
| --------- | ------------------------------------------- |
| category  | Filter products by category                 |
| cursor_id | Fetch the next page using cursor pagination |
| limit     | Number of products to return                |

Example:

```text
GET /products?category=Books

GET /products?cursor_id=400981

GET /products?limit=20
```

---

## Project Structure

```text
app/
├── database.py
├── main.py
├── models.py
├── routes.py
└── templates/
    └── index.html

scripts/
└── seed.py

requirements.txt
README.md
```

---

## Running the Project

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the server:

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## About Cursor Pagination

Instead of using OFFSET, this project uses cursor-based pagination with the product ID. This keeps pagination efficient for large datasets and provides a consistent browsing experience even when new products are added while a user is browsing.

---

## Future Improvements

If I had more time, I would like to add:

* Product search
* Sorting by price and date
* Authentication
* Unit tests
* Docker support
* CI/CD pipeline

---

## Author

**Durga Roy**
