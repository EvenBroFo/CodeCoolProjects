class BaseProduct:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def apply_discount(self, discount_percentage): 
        discount_value = self.price * (discount_percentage / 100)
        self.price -= discount_value

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}"