from typing import List
from src.domain.models.orders import Order
from src.infra.db.entities.orders import Order as OrderModel
from src.infra.db.settings.connection import DBConnectionHandler

class OrdersRepository:
    def __init__(self):
        self.db_connection_handler = DBConnectionHandler()

    def insert_order(self, order_id, customer_id, order_timestamp, total_amount):
        with self.db_connection_handler as db:
            order = OrderModel(
                order_id=order_id,
                customer_id=customer_id,
                order_timestamp=order_timestamp,
                total_amount=total_amount  # Add this line to include the total_amount
            )
            db.session.add(order)
            db.session.commit()

    def select_order(self, order_id: str) -> List[Order]:
        with self.db_connection_handler as db:
            orders = db.session.query(OrderModel).filter_by(order_id=order_id).all()
            return [Order(
                order_id=order.order_id,
                customer_id=order.customer_id,
                order_timestamp=order.order_timestamp,
                total_amount=order.total_amount
            ) for order in orders]
