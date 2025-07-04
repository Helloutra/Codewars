def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    if not text:
        return ''
    for char in text:
        if char not in alphabet and char != ' ':
            text = text.replace(char, '')
    position = [str(alphabet.index(char) + 1) for char in text if char != ' ']
    return ' '.join(position)