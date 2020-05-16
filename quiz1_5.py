def compute_sum(n):
    if n == 1:
        return n
    if n < 1:
        return ValueError
    else:
        return n + compute_sum(n-1)
    return n

print(compute_sum(3))