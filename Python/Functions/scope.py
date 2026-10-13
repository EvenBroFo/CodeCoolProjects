counter = 1

#while counter <= 10:
#   text = f"Iteration {counter}"
#   print(text)
#   counter += 1

#print(f"outside: {text}")

def greet_somebody(name):
    greeting = f"hello {name}"
    return(greeting)

#greet_somebody("Even") --> since return in function not print, it does not print
#print(greeting) --> not defined because it is defined in function. 

print(greet_somebody("Even")) 