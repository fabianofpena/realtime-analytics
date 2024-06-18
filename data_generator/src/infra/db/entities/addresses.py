from sqlalchemy import Column, String, ForeignKey
from src.infra.db.settings.base import Base

class Address(Base):
    __tablename__ = "addresses"

    address_id = Column(String(36), primary_key=True)
    customer_id = Column(String(36), ForeignKey('customers.customer_id'), nullable=False)
    street = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zipcode = Column(String(20), nullable=False)
    country = Column(String(50), nullable=False)

    def __repr__(self):
        return f"Address [address_id={self.address_id}, city={self.city}]"
