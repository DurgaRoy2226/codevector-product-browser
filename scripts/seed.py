from random import choice, uniform
from datetime import datetime

from app.database import SessionLocal
from app.models import Product

db = SessionLocal()

products_catalog = {
    "Electronics": [
        "Apple MacBook Air M2",
        "Dell XPS 13",
        "Samsung Galaxy S24",
        "iPhone 15",
        "Sony WH-1000XM5",
        "Logitech MX Master 3S"
    ],
    "Books": [
        "Atomic Habits",
        "Deep Work",
        "Clean Code",
        "Rich Dad Poor Dad",
        "Python for Data Science",
        "The Psychology of Money"
    ],
    "Sports": [
        "Nike Running Shoes",
        "Cricket Bat",
        "Football",
        "Yoga Mat",
        "Dumbbell Set",
        "Tennis Racket"
    ],
    "Home": [
        "Office Chair",
        "Study Table",
        "LED Desk Lamp",
        "Wall Clock",
        "Coffee Table",
        "Bookshelf"
    ],
    "Clothing": [
        "Polo T-Shirt",
        "Denim Jeans",
        "Hoodie",
        "Formal Shirt",
        "Jacket",
        "Sneakers"
    ]
}

BATCH_SIZE = 5000
TOTAL_RECORDS = 200000

for start in range(0, TOTAL_RECORDS, BATCH_SIZE):

    products = []

    for _ in range(BATCH_SIZE):

        category = choice(list(products_catalog.keys()))

        products.append(
            Product(
                name=choice(products_catalog[category]),
                category=category,
                price=round(uniform(500, 100000), 2),
                created_at=datetime.utcnow(),
                updated_at=datetime.utcnow()
            )
        )

    db.bulk_save_objects(products)
    db.commit()

    print(f"Inserted {start + BATCH_SIZE} products")

print("Finished inserting 200000 products")