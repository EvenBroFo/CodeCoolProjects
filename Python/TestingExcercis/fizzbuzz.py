def fizzbuzz(n):
    if type(n) is not int or n <= 0:
        raise ValueError("Input must be a positive integer")

    results = []

    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            results.append("FizzBuzz")
        elif number % 3 == 0:
            results.append("Fizz")
        elif number % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(number))

    return results