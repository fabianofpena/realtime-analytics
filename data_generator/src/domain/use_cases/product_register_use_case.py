from typing import Dict
from faker import Faker
from src.interfaces.product_register import ProductRegister
from src.infra.repositories.products_repository import ProductsRepository

class ProductRegisterUseCase(ProductRegister):
    def __init__(self, product_repository: ProductsRepository):
        self.product_repository = product_repository
        self.fake = Faker()

    def register(self, product_name: str = None, category: str = None, price: float = None, stock_quantity: int = None) -> Dict:
        if not product_name:
            product_name = self.fake.word()
        if not category:
            category = self.fake.word()
        if not price:
            price = round(self.fake.random_float(min=10.0, max=1000.0), 2)
        if not stock_quantity:
            stock_quantity = self.fake.random_int(min=0, max=1000)
        
        self.product_repository.insert_product(product_name, category, price, stock_quantity)
        return {
            "product_name": product_name,
            "category": category,
            "price": price,
            "stock_quantity": stock_quantity
        }
