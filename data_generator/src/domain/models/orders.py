class Order:
    def __init__(self, order_id: str, customer_id: str, order_timestamp: str, total_amount: float) -> None:
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_timestamp = order_timestamp
        self.total_amount = total_amount
