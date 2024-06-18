from typing import List
from src.domain.models.order_items import OrderItem
from src.infra.db.entities.order_items import OrderItem as OrderItemModel
from src.infra.db.settings.connection import DBConnectionHandler

class OrderItemsRepository:
    def __init__(self):
        self.db_connection_handler = DBConnectionHandler()

    def insert_order_item(self, order_item_id, order_id, product_id, quantity, price):
        with self.db_connection_handler as db:
            order_item = OrderItemModel(
                order_item_id=order_item_id,
                order_id=order_id,
                product_id=product_id,
                quantity=quantity,
                price=price  # Add this line to include the price
            )
            db.session.add(order_item)
            db.session.commit()

    def select_order_item(self, order_item_id: str) -> List[OrderItem]:
        with self.db_connection_handler as db:
            order_items = db.session.query(OrderItemModel).filter_by(order_item_id=order_item_id).all()
            return [OrderItem(
                order_item_id=order_item.order_item_id,
                order_id=order_item.order_id,
                product_id=order_item.product_id,
                quantity=order_item.quantity,
                price=order_item.price
            ) for order_item in order_items]
