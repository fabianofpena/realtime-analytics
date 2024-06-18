class Address:
    def __init__(self, address_id: str, customer_id: str, street: str, city: str, state: str, zipcode: str, country: str) -> None:
        self.address_id = address_id
        self.customer_id = customer_id
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.country = country
