products = [
    { "name" : "White Tea", "Price" : 123.5, "Quantity" : 50, "Location" : "Store A"},
    { "name" : "Green Tea", "Price" : 133.5, "Quantity" : 5, "Location" : "Store B"},
    { "name" : "Black Tea", "Price" : 140.5, "Quantity" : 15, "Location" : "Store C"}
]

def is_in_stock(product):
    return product["Quantity"] > 0

def apply_discount(product, discount_percentage):
    discount_amount = (discount_percentage/100) * product["Price"]
    product["Price"] -= discount_amount

def restock(product, additional_quantity):
    product["Quantity"] += additional_quantity


for product in products:
    print(is_in_stock(product))

apply_discount(products[1], 10)
print(product[1]["Price"])

restock(products[2], 25)
print(products[2]["Quantity"])

