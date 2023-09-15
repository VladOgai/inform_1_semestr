lst = list(map(int, input().split()))
num = 0
nummax = 0
for l in lst:
    if lst.count(l) > nummax:
        nummax = lst.count(l)
        num = l
print(num)