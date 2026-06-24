from fastapi import APIRouter
from app.database import SessionLocal
from app.models import Product

router = APIRouter()


@router.get("/products")
def get_products(
    category: str = None,
    cursor_id: int = None,
    limit: int = 20
):
    db = SessionLocal()

    try:
        query = db.query(Product)

        if category:
            query = query.filter(
                Product.category == category
            )

        if cursor_id:
            query = query.filter(
                Product.id < cursor_id
            )

        products = (
            query
            .order_by(
                Product.updated_at.desc(),
                Product.id.desc()
            )
            .limit(limit)
            .all()
        )

        next_cursor = None

        if products:
            next_cursor = products[-1].id

        return {
            "next_cursor": next_cursor,
            "count": len(products),
            "products": [
                {
                    "id": p.id,
                    "name": p.name,
                    "category": p.category,
                    "price": p.price,
                    "updated_at": p.updated_at
                }
                for p in products
            ]
        }

    finally:
        db.close()