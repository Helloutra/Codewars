def disemvowel(string_):
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in string_:
        if char not in vowels:
            new_string += char
    return new_string