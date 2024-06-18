from typing import Dict
from faker import Faker
import uuid
from src.interfaces.customer_register import CustomerRegister
from src.infra.repositories.customers_repository import CustomersRepository
from src.infra.repositories.addresses_repository import AddressesRepository

class CustomerRegisterUseCase(CustomerRegister):
    def __init__(self, customer_repository: CustomersRepository, address_repository: AddressesRepository):
        self.customer_repository = customer_repository
        self.address_repository = address_repository
        self.fake = Faker()

    def register(self, customer_name: str = None, email: str = None, phone_number: str = None) -> Dict:
        customer_id = str(uuid.uuid4())
        if not customer_name:
            customer_name = self.fake.name()
        if not email:
            email = self.fake.email()
        if not phone_number:
            phone_number = self.fake.phone_number()[:20]  # Truncate the phone number to 20 characters

        self.customer_repository.insert_customer(customer_id, customer_name, email, phone_number, None)
        
        # Create and insert the address using the customer_id
        address_id = str(uuid.uuid4())
        self.address_repository.insert_address(
            address_id,
            customer_id,
            self.fake.street_address(),
            self.fake.city(),
            self.fake.state(),
            self.fake.zipcode(),
            self.fake.country()
        )

        # Update the customer record with the newly created address_id
        self.customer_repository.update_customer_address(customer_id, address_id)

        return {
            "customer_id": customer_id,
            "customer_name": customer_name,
            "email": email,
            "phone_number": phone_number,
            "address_id": address_id
        }