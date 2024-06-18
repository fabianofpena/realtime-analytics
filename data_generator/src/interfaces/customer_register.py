from abc import ABC, abstractmethod
from typing import Dict

class CustomerRegister(ABC):

    @abstractmethod
    def register(self, customer_name: str, email: str, phone_number: str, address_id: str) -> Dict: 
        pass
