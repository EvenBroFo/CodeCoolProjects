def form_the_minimum(numbers):
    unique_numbers = set(numbers)
    sorted_numbers = sorted(unique_numbers)
    result = "".join(str(number) for number in sorted_numbers)

    return int(result)

print(form_the_minimum("4213456"))
