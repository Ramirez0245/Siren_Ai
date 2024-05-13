import string


def find_numbers_as_text(text):
    numbers_mapping = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
    }

    tokens = text.split()
    updated_tokens = []

    for token in tokens:
        if token.lower() in numbers_mapping:
            updated_tokens.append(str(numbers_mapping[token.lower()]))
        else:
            updated_tokens.append(token)

    updated_text = " ".join(updated_tokens)
    return updated_text
