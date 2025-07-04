from preloaded import MORSE_CODE

def decode_morse(morse_code):
    mots = morse_code.strip().split(' ')
    decoded_message = []
    for lettre in mots:
        if lettre == '':
            decoded_message.append(' ')
        else:
            decoded_message.append(MORSE_CODE[lettre])
    return ''.join(decoded_message).replace('  ', ' ')

