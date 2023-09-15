_ = int(input())
lst = list(map(int, input().split()))
m = 0
b = 0
for l in lst:
    for j in lst:
        if j == l:
            continue
        elif j < l:
            m += 1
        elif j > l:
            b += 1
    if m == b:
        print(l)
        break
    m = 0
    b = 0