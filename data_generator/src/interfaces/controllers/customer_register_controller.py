from src.interfaces.customer_register import CustomerRegister
from typing import Dict

class CustomerRegisterController:
    def __init__(self, customer_register: CustomerRegister):
        self.customer_register = customer_register

    def register_customer(self, customer_name: str = None, email: str = None, phone_number: str = None) -> Dict:
        return self.customer_register.register(customer_name, email, phone_number)
