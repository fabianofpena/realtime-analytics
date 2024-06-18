from typing import Dict
from faker import Faker
import uuid
from src.interfaces.order_register import OrderRegister
from src.infra.repositories.orders_repository import OrdersRepository

class OrderRegisterUseCase(OrderRegister):
    def __init__(self, order_repository: OrdersRepository):
        self.order_repository = order_repository
        self.fake = Faker()

    def register(self, customer_id: str, order_timestamp: str = None, total_amount: float = None) -> Dict:
        order_id = str(uuid.uuid4())
        if not order_timestamp:
            order_timestamp = self.fake.date_time_this_year().isoformat()
        if not total_amount:
            total_amount = round(self.fake.random.uniform(10.0, 5000.0), 2)

        self.order_repository.insert_order(order_id, customer_id, order_timestamp, total_amount)

        return {
            "order_id": order_id,
            "customer_id": customer_id,
            "order_timestamp": order_timestamp,
            "total_amount": total_amount
        }