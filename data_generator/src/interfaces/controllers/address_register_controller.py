from src.interfaces.address_register import AddressRegister
from typing import Dict

class AddressRegisterController:
    def __init__(self, address_register: AddressRegister):
        self.address_register = address_register

    def register_address(self, customer_id: str = None, street: str = None, city: str = None, state: str = None, zipcode: str = None, country: str = None) -> Dict:
        return self.address_register.register(customer_id, street, city, state, zipcode, country)
