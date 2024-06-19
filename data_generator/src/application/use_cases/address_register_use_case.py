from typing import Dict
from faker import Faker
import uuid
from src.interfaces.address_register import AddressRegister
from src.infra.repositories.addresses_repository import AddressesRepository

class AddressRegisterUseCase(AddressRegister):
    def __init__(self, address_repository: AddressesRepository):
        self.address_repository = address_repository
        self.fake = Faker()

    def register(self, customer_id: str = None, street: str = None, city: str = None, state: str = None, zipcode: str = None, country: str = None) -> Dict:
        address_id = str(uuid.uuid4())
        if not customer_id:
            customer_id = self.fake.uuid4()
        if not street:
            street = self.fake.street_address()
        if not city:
            city = self.fake.city()
        if not state:
            state = self.fake.state()
        if not zipcode:
            zipcode = self.fake.zipcode()
        if not country:
            country = self.fake.country()
        
        # Truncate country to 50 characters
        country = country[:50]
        
        self.address_repository.insert_address(address_id, customer_id, street, city, state, zipcode, country)
        return {
            "address_id": address_id,
            "customer_id": customer_id,
            "street": street,
            "city": city,
            "state": state,
            "zipcode": zipcode,
            "country": country
        }
