lst = list(input().split())
s = []
while lst != []:
    a = lst[0]
    if lst.count(a) == 1:
        s.append(a)
        lst.remove(a)
    else:
        for _ in range(lst.count(a)):
            lst.remove(a)
print(*s)