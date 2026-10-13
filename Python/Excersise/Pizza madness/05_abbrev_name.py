def abbrev_name(name):
    words = name.split()

    first_initial = words[0][0].upper()
    second_initial = words[1][0].upper()

    return first_initial + "." + second_initial


print(abbrev_name("Hawaii Pizza"))