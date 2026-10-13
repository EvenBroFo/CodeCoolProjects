def calculate_total(order_amount, shipping_fee = 20):
    discount = 0.15 if order_amount > 200 else 0.05
    total = (order_amount - (order_amount*discount)) + shipping_fee
    return total

#order_amount = 1000
#shipping_fee = 20
#discount = 0.15 if order_amount > 200 else 0.05
#total = (order_amount - (order_amount*discount)) + shipping_fee

#print(f"Order amount: {order_amount}")
#print(f"Discount applied: {discount * 100} %")
#print(f"Shipping fee: {shipping_fee}")
#print(f"Total: {total}")
#print()

#order_amount = 100
#shipping_fee = 25
#discount = 0.15 if order_amount > 200 else 0.05
#total = (order_amount - (order_amount*discount)) + shipping_fee

#print(f"Order amount: {order_amount}")
#print(f"Discount applied: {discount * 100} %")
#print(f"Shipping fee: {shipping_fee}")
#print(f"Total: {total}")
#print()

#order_amount = 1200
#shipping_fee = 20
#discount = 0.15 if order_amount > 200 else 0.05
#total = (order_amount - (order_amount*discount)) + shipping_fee

#print(f"Order amount: {order_amount}")
#print(f"Discount applied: {discount * 100} %")
#print(f"Shipping fee: {shipping_fee}")
#print(f"Total: {total}")
#print()

order_amount = 1000
shipping_fee = 20
total = calculate_total(order_amount, shipping_fee)

print(f"Total: {total}")

total2 = calculate_total(1200, 20)
print(f"total2: {total2}")

total3 = calculate_total(100)

print(f"total3: {total3}")