def is_isogram(string):
    déjà_vu = set()
    for char in string:
        if char in déjà_vu:
            return False
        déjà_vu.add(char.lower())
        déjà_vu.add(char.upper())
    return True