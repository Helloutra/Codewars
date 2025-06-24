def find_uniq(arr):
    counts = {}
    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    for num, count in counts.items():
        if count == 1:
            return num