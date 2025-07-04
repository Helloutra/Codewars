def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    x = 0
    y = 0
    for direction in walk:
        if direction == 'n':
            x +=1
        elif direction == 's':
            x -= 1
        elif direction == 'e':
            y += 1
        elif direction == 'w':
            y -= 1
    if x != 0 or y != 0:
        return False
    else:
        return True