def tri(s, b):
    for i in range(1, s + 1):
        print(b * min(i, s - i + 1))

tri(9, 'C')