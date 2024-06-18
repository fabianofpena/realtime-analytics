from src.domain.use_cases.product_register import ProductRegister
from src.presentation.interfaces.controller_interface import ControllerInterface
from typing import Dict

class ProductRegisterController(ControllerInterface):
    def __init__(self, product_register: ProductRegister):
        self.product_register = product_register

    def handle(self, request: Dict) -> Dict:
        product_name = request.get("product_name")
        category = request.get("category")
        price = request.get("price")
        stock_quantity = request.get("stock_quantity")
        return self.product_register.register(product_name, category, price, stock_quantity)
