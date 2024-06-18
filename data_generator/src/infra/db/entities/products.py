from sqlalchemy import Column, String, Integer, Float
from src.infra.db.settings.base import Base

class Product(Base):
    __tablename__ = "products"

    product_id = Column(String(36), primary_key=True)
    product_name = Column(String(50), nullable=False)
    category = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    stock_quantity = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Product [product_id={self.product_id}, product_name={self.product_name}]"
