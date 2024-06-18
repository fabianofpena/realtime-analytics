from typing import Dict
from faker import Faker
import uuid
from src.interfaces.order_item_register import OrderItemRegister
from src.infra.repositories.order_items_repository import OrderItemsRepository
from src.infra.repositories.products_repository import ProductsRepository

class OrderItemRegisterUseCase(OrderItemRegister):
    def __init__(self, order_item_repository: OrderItemsRepository, product_repository: ProductsRepository):
        self.order_item_repository = order_item_repository
        self.product_repository = product_repository
        self.fake = Faker()

    def register(self, order_id: str = None, product_id: str = None, quantity: int = None, price: float = None) -> Dict:
        order_item_id = str(uuid.uuid4())
        if not order_id:
            order_id = str(uuid.uuid4())
        if not product_id:
            product_id = str(uuid.uuid4())
            # Insert a dummy product if it doesn't exist
            self.product_repository.insert_product(
                product_id, 
                self.fake.word(), 
                self.fake.word(), 
                round(self.fake.random.uniform(10.0, 1000.0), 2), 
                self.fake.random_int(min=0, max=1000)
            )
        if not quantity:
            quantity = self.fake.random_int(min=1, max=10)
        if not price:
            price = round(self.fake.random.uniform(10.0, 1000.0), 2)

        self.order_item_repository.insert_order_item(order_item_id, order_id, product_id, quantity, price)
        return {
            "order_item_id": order_item_id,
            "order_id": order_id,
            "product_id": product_id,
            "quantity": quantity,
            "price": price
        }
