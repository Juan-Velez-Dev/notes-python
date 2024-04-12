""" Funcion palindroma """


def no_space(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text


def reverse(text):
    reverse_text = ""
    for char in text:
        reverse_text = char + reverse_text
    return reverse_text


def palindrome(text):
    text = no_space(text)
    reverse_text = reverse(text)
    return text.lower() == reverse_text.lower()


print(palindrome("amo la paloma"))
