def basic_operations(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "divide":
        return num1 / num2
    elif operation == "multiply":
        return num1 * num2

print(basic_operations("add", 2, 3))
print(basic_operations("subtract", 4, 10))
print(basic_operations("divide", 40, 4))
print(basic_operations("multiply", 0.5, 3))