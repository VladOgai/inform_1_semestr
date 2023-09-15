slist = list(map(int, input().split()))
n = slist.pop(0)
s = (n + 1) * n / 2
for i in slist:
    s -= i
print(int(s))