from typing import Optional

from fastapi import APIRouter
from app.database import SessionLocal
from app.models import Product

router = APIRouter()


@router.get(
    "/products",
    summary="Browse products with cursor pagination"
)
def get_products(
    category: Optional[str] = None,
    cursor_id: Optional[int] = None,
    limit: int = 20
):
    db = SessionLocal()

    try:

        # Prevent very large requests
        if limit < 1:
            limit = 20

        if limit > 100:
            limit = 100

        query = db.query(Product)

        # Category filter
        if category:
            query = query.filter(
                Product.category == category
            )

        # Cursor pagination
        if cursor_id is not None:
            query = query.filter(
                Product.id < cursor_id
            )

        # Newest products first
        products = (
            query
            .order_by(Product.id.desc())
            .limit(limit)
            .all()
        )

        next_cursor = (
            products[-1].id
            if products
            else None
        )

        return {
            "next_cursor": next_cursor,
            "count": len(products),
            "products": [
                {
                    "id": p.id,
                    "name": p.name,
                    "category": p.category,
                    "price": p.price,
                    "created_at": p.created_at,
                    "updated_at": p.updated_at
                }
                for p in products
            ]
        }

    finally:
        db.close()