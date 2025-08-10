def remov_nb(n):
    égal = []
    total = n * (n + 1) // 2
    for a in range(1, n + 1):
        b = (total - a) / (a+1)
        if b == int(b) and 1 <= b <= n+1 and a != b:
            égal.append((a, int(b)))
    return égal