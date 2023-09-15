a = list(input().split())
b = [a[i + 1] + ' ' + a[i] for i in range(0, len(a) - 1, 2)]
b.append(a[-1]) if len(a) % 2 == 1 else None
print(*b)