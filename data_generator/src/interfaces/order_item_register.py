from abc import ABC, abstractmethod
from typing import Dict

class OrderItemRegister(ABC):

    @abstractmethod
    def register(self, order_id: str, product_id: str, quantity: int, price: float) -> Dict: 
        pass
