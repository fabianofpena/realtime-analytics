from typing import List
from src.domain.models.products import Product
from src.infra.db.entities.products import Product as ProductModel
from src.infra.db.settings.connection import DBConnectionHandler

class ProductsRepository:
    def __init__(self):
        self.db_connection_handler = DBConnectionHandler()

    def insert_product(self, product_id: str, product_name: str, category: str, price: float, stock_quantity: int) -> None:
        with self.db_connection_handler as db:
            product = ProductModel(
                product_id=product_id,
                product_name=product_name,
                category=category,
                price=price,
                stock_quantity=stock_quantity
            )
            db.session.add(product)
            db.session.commit()

    def select_product(self, product_name: str) -> List[Product]:
        with self.db_connection_handler as db:
            products = db.session.query(ProductModel).filter_by(product_name=product_name).all()
            return [Product(
                product_id=product.product_id,
                product_name=product.product_name,
                category=product.category,
                price=product.price,
                stock_quantity=product.stock_quantity
            ) for product in products]
