from sqlalchemy import Column, String, ForeignKey
from src.infra.db.settings.base import Base

class Customer(Base):
    __tablename__ = "customers"
    
    customer_id = Column(String(36), primary_key=True)
    customer_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phone_number = Column(String(30), nullable=False)  # Increase the length here
    address_id = Column(String(36), ForeignKey('addresses.address_id'), nullable=True)

    def __repr__(self):
        return f"Customer [customer_id={self.customer_id}, customer_name={self.customer_name}]"