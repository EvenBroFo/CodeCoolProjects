def largest_number(a, b, c):
    results = [
        a + b + c,
        a * b * c,
        (a + b) * c,
        a * (b + c),
        a + b * c,
        a * b + c
    ]

    return max(results)


print(largest_number(1, 2, 3))