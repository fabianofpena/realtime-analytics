from sqlalchemy import create_engine, Column, String, Integer, Float, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'mysql+mysqlconnector://username:password@localhost:3306/your_database'
engine = create_engine(DATABASE_URI)
Base = declarative_base()

class ProductModel(Base):
    __tablename__ = 'products'
    product_id = Column(String(36), primary_key=True)
    product_name = Column(String(50))
    category = Column(String(50))
    price = Column(Float)
    stock_quantity = Column(Integer)

class CustomerModel(Base):
    __tablename__ = 'customers'
    customer_id = Column(String(36), primary_key=True)
    customer_name = Column(String(50))
    email = Column(String(50))
    phone_number = Column(String(20))
    address_id = Column(String(36), ForeignKey('addresses.address_id'))

class OrderModel(Base):
    __tablename__ = 'orders'
    order_id = Column(String(36), primary_key=True)
    customer_id = Column(String(36), ForeignKey('customers.customer_id'))
    order_timestamp = Column(TIMESTAMP)
    total_amount = Column(Float)

class OrderItemModel(Base):
    __tablename__ = 'order_items'
    order_item_id = Column(String(36), primary_key=True)
    order_id = Column(String(36), ForeignKey('orders.order_id'))
    product_id = Column(String(36), ForeignKey('products.product_id'))
    quantity = Column(Integer)
    price = Column(Float)

class AddressModel(Base):
    __tablename__ = 'addresses'
    address_id = Column(String(36), primary_key=True)
    customer_id = Column(String(36), ForeignKey('customers.customer_id'))
    street = Column(String(100))
    city = Column(String(50))
    state = Column(String(50))
    zipcode = Column(String(20))
    country = Column(String(50))

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
