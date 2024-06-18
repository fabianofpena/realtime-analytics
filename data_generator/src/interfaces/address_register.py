from abc import ABC, abstractmethod
from typing import Dict

class AddressRegister(ABC):

    @abstractmethod
    def register(self, customer_id: str, street: str, city: str, state: str, zipcode: str, country: str) -> Dict: 
        pass
