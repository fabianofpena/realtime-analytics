from abc import ABC, abstractmethod
from typing import Dict

class OrderRegister(ABC):

    @abstractmethod
    def register(self, customer_id: str, order_timestamp: str, total_amount: float) -> Dict: 
        pass
