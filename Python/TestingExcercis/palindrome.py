def is_palindrome(text):
    cleaned_text = ""

    for char in text:
        if char.isalnum():
            cleaned_text += char.lower()
    return cleaned_text == cleaned_text[::-1]

