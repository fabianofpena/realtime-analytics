class Product:
    def __init__(self, product_id: str, product_name: str, category: str, price: float, stock_quantity: int) -> None:
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
