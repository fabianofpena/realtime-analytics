class OrderItem:
    def __init__(self, order_item_id: str, order_id: str, product_id: str, quantity: int, price: float) -> None:
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
