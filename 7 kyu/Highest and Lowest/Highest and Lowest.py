def high_and_low(numbers):
    num_list = list(map(int, numbers.split()))
    num_max = max(num_list)
    num_min = min(num_list)
    return f"{num_max} {num_min}"