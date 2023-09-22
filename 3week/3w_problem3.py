def euclid(a: int, b: int) -> tuple:
    if b == 0:
        return 1, 0, a
    y, x, d = euclid(b, a % b)
    return x, y - (a // b) * x, d


a, b = map(int, input().split())
print(*euclid(a, b))