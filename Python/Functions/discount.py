def calculate_total_and_discount(order_amount, shipping_fee = 20):
    discount = 0.15 if order_amount > 200 else 0.05
    total = (order_amount - (order_amount * discount)) + shipping_fee
    return total, discount

my_total, my_discount = calculate_total_and_discount(2000, 100)

print(f"My total = {my_total}")
print(f"My discount = {my_discount * 100}%")

red = (255, 0, 0)
geen = (0, 255, 0)
blue = (0, 0, 255)

#red[0] = 150 --> cant change the value when its tuple

print(red[0])