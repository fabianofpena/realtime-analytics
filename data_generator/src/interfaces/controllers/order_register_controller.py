from src.interfaces.order_register import OrderRegister
from typing import Dict

class OrderRegisterController:
    def __init__(self, order_register: OrderRegister):
        self.order_register = order_register

    def register_order(self, customer_id: str = None, order_timestamp: str = None, total_amount: float = None) -> Dict:
        return self.order_register.register(customer_id, order_timestamp, total_amount)
