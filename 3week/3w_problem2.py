def prime(n, i = 2):
    s = 0
    if n == 1:
        return ''
    while n % i == 0:
        s += 1
        n /= i
    if s == 0:
        return prime(n, i + 1)
    return (prime(n, i + 1) + f' {i}x{s}').lstrip()