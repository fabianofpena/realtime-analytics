from typing import List
from src.domain.models.addresses import Address
from src.infra.db.entities.addresses import Address as AddressModel
from src.infra.db.settings.connection import DBConnectionHandler

class AddressesRepository:
    def __init__(self):
        self.db_connection_handler = DBConnectionHandler()

    def insert_address(self, address_id: str, customer_id: str, street: str, city: str, state: str, zipcode: str, country: str) -> None:
        with self.db_connection_handler as db:
            address = AddressModel(
                address_id=address_id,
                customer_id=customer_id,
                street=street,
                city=city,
                state=state,
                zipcode=zipcode,
                country=country
            )
            db.session.add(address)
            db.session.commit()

    def select_address(self, address_id: str) -> List[Address]:
        with self.db_connection_handler as db:
            addresses = db.session.query(AddressModel).filter_by(address_id=address_id).all()
            return [Address(
                address_id=address.address_id,
                customer_id=address.customer_id,
                street=address.street,
                city=address.city,
                state=address.state,
                zipcode=address.zipcode,
                country=address.country
            ) for address in addresses]
