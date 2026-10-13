class Order:
    def __init__(self):
        self.order_items = []

    def add_product(self, product):
        self.order_items.append(product)

    def display_details(self):
        for item in self.order_items:
            print(item)

    