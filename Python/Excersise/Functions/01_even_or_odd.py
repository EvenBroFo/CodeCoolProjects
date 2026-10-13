def even_or_odd(number):
    if number % 2 == 0:
        return("even")
    else:
        return("Odd")

print("this number is", even_or_odd(1))
print(f"this number is {even_or_odd(2322)}")