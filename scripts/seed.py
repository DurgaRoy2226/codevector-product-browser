from faker import Faker
from random import choice, uniform
from datetime import datetime, timedelta

from app.database import SessionLocal
from app.models import Product

fake = Faker()

db = SessionLocal()

categories = [
    "Electronics",
    "Books",
    "Sports",
    "Home",
    "Clothing"
]

BATCH_SIZE = 10000
TOTAL_PRODUCTS = 200000

for batch_start in range(0, TOTAL_PRODUCTS, BATCH_SIZE):

    products = []

    for _ in range(BATCH_SIZE):

        created_time = fake.date_time_between(
            start_date="-365d",
            end_date="now"
        )

        updated_time = created_time + timedelta(
            days=choice(range(0, 30))
        )

        products.append(
            Product(
                name=fake.word(),
                category=choice(categories),
                price=round(uniform(100, 100000), 2),
                created_at=created_time,
                updated_at=updated_time
            )
        )

    db.bulk_save_objects(products)
    db.commit()

    print(
        f"Inserted {batch_start + BATCH_SIZE}/{TOTAL_PRODUCTS}"
    )

db.close()

print("✅ Inserted 200000 products")