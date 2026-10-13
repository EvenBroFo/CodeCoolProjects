def name_length(name):
    words = name.split()
    result = []

    for word in words:
        result.append(f"{word} {len(word)}")

    return result


print(name_length("hawaii pizza"))