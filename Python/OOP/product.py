from BaseProduct import BaseProduct

class Product(BaseProduct):
    name = ""
    price = 0
    quantity = 0
    location = ""
    weight = 0
    description = ""

    def __init__(self, name, price, quantity, location, weight, description):
        super().__init__(name, price, description)
        self.quantity = quantity
        self.location = location
        self.weight = weight


    def is_in_stock(self):
        return self.quantity > 0

    def get_total_value(self):
        return self.price 

    def restock(self, additional_quantity):
        self.quantity += additional_quantity

    @staticmethod
    def is_valid_product_name(name):
        return isinstance(name, str) and len(name) > 0

    def __str__(self):
        return(f"Product name: {self.name}, price: {self.price}, Location: {self.location}")

    