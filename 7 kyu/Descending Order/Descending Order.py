def descending_order(num):
    num_str = str(num)
    sorted_digits = sorted(num_str, reverse=True)
    return int(''.join(sorted_digits))