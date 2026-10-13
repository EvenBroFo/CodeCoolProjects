def average(*args): #Positional
    return sum(args) / len(args)

print(average(1,2,5,8,10))


def greet(**kwargs): #keyword args
    for key, value in kwargs.items():
        print(f"{key} {value}")

greet(name="alice", age = 25, city="new york")
greet(name="bob", occupation="engineer")

print("d","e","w","q", sep="---")