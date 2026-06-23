from sqlalchemy import Column, Integer, String, Float, DateTime, Index

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    category = Column(String, nullable=False)

    price = Column(Float, nullable=False)

    created_at = Column(DateTime, nullable=False)

    updated_at = Column(DateTime, nullable=False)

    __table_args__ = (
        Index(
            "idx_products_updated_id",
            "updated_at",
            "id"
        ),
        Index(
            "idx_products_category_updated_id",
            "category",
            "updated_at",
            "id"
        ),
    )