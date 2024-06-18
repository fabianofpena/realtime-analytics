from sqlalchemy import Column, String, Integer, Float, ForeignKey
from src.infra.db.settings.base import Base

class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(String(36), primary_key=True)
    order_id = Column(String(36), ForeignKey('orders.order_id'), nullable=False)
    product_id = Column(String(36), ForeignKey('products.product_id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return f"OrderItem [order_item_id={self.order_item_id}, quantity={self.quantity}]"
