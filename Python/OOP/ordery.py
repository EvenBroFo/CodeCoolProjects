from product import Product
from VirtualProduct import VirtualProduct
from Order import Order

white_tea = Product("White Tea", 100, 20, "Store A", 10)

e_book = VirtualProduct("The Hail Mary Project", 50,  "https://download.link")

my_order = Order()

my_order.add_product(white_tea)
my_order.add_product(e_book)

my_order.display_details()