from fastapi import APIRouter
from app.database import SessionLocal
from app.models import Product

router = APIRouter()


@router.get("/products")
def get_products(
    category: str = None,
    cursor_id: int = None
):

    db = SessionLocal()

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
        .order_by(Product.id.desc())
        .limit(20)
        .all()
    )

    return [
        {
            "id": p.id,
            "name": p.name,
            "category": p.category,
            "price": p.price
        }
        for p in products
    ]