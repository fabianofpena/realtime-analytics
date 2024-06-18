class Customer:
    def __init__(self, customer_id: str, customer_name: str, email: str, phone_number: str, address_id: str) -> None:
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number
        self.address_id = address_id