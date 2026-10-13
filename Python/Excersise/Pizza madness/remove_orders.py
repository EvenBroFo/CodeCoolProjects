def remove_orders(orders):
    numbers = orders.split(",")

    remaining = numbers[1:-1]

    return ",".join(remaining)


print(remove_orders("1,2,3,4"))