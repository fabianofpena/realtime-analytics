from sqlalchemy import Column, String, Float, TIMESTAMP, ForeignKey
from src.infra.db.settings.base import Base

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(String(36), primary_key=True)
    customer_id = Column(String(36), ForeignKey('customers.customer_id'), nullable=False)
    order_timestamp = Column(TIMESTAMP, nullable=False)
    total_amount = Column(Float, nullable=False)

    def __repr__(self):
        return f"Order [order_id={self.order_id}, total_amount={self.total_amount}]"
