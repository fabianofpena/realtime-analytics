from src.interfaces.order_item_register import OrderItemRegister
from typing import Dict

class OrderItemRegisterController:
    def __init__(self, order_item_register: OrderItemRegister):
        self.order_item_register = order_item_register

    def register_order_item(self, order_id: str = None, product_id: str = None, quantity: int = None, price: float = None) -> Dict:
        return self.order_item_register.register(order_id, product_id, quantity, price)
