products = [
    { "name" : "White Tea", "Price" : 123.5, "Quantity" : 50, "location" : "Store A"},
    { "name" : "Green Tea", "Price" : 133.5, "Quantity" : 5, "location" : "Store B"},
    { "name" : "Black Tea", "Price" : 140.5, "Quantity" : 15, "location" : "Store A"}
]

unique_locations = set()

for product in products:
    unique_locations.add(product["location"])

print(unique_locations)