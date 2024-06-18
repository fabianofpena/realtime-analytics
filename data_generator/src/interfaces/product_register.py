from abc import ABC, abstractmethod
from typing import Dict

class ProductRegister(ABC):

    @abstractmethod
    def register(self, product_name: str, category: str, price: float, stock_quantity: int) -> Dict: 
        pass
