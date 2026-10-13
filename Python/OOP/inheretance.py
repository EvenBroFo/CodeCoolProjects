from product import Product
from VirtualProduct import VirtualProduct
from BaseProduct import BaseProduct

white_tea = Product("White Tea", 100, 20, "Store A", 10)

e_book = VirtualProduct("The Hail Mary Project", 50,  "https://download.link")


products = {white_tea, e_book}

for product in products:
    print(product)

