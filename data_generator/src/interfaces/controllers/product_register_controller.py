from src.interfaces.product_register import ProductRegister
from typing import Dict

class ProductRegisterController:
    def __init__(self, product_register: ProductRegister):
        self.product_register = product_register

    def register_product(self, product_name: str = None, category: str = None, price: float = None, stock_quantity: int = None) -> Dict:
        return self.product_register.register(product_name, category, price, stock_quantity)
