from typing import List
from src.domain.models.customers import Customer
from src.infra.db.entities.customers import Customer as CustomerModel
from src.infra.db.settings.connection import DBConnectionHandler

class CustomersRepository:
    def __init__(self):
        self.db_connection_handler = DBConnectionHandler()

    def insert_customer(self, customer_id: str, customer_name: str, email: str, phone_number: str, address_id: str) -> None:
        with self.db_connection_handler as db:
            customer = CustomerModel(
                customer_id=customer_id, 
                customer_name=customer_name, 
                email=email, 
                phone_number=phone_number, 
                address_id=address_id
            )
            db.session.add(customer)
            db.session.commit()

    def update_customer_address(self, customer_id: str, address_id: str) -> None:
        with self.db_connection_handler as db:
            customer = db.session.query(CustomerModel).filter_by(customer_id=customer_id).first()
            if customer:
                customer.address_id = address_id
                db.session.commit()

    def select_customer(self, customer_name: str) -> List[Customer]:
        with self.db_connection_handler as db:
            customers = db.session.query(CustomerModel).filter_by(customer_name=customer_name).all()
            return [
                Customer(
                    customer_id=customer.customer_id,
                    customer_name=customer.customer_name,
                    email=customer.email,
                    phone_number=customer.phone_number,
                    address_id=customer.address_id
                ) for customer in customers
            ]
