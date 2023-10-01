lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

# 1
s1 = set(lst1)
s2 = set(lst2)
print(*s1)
print(*s2)

# 2
s3 = s1.copy()
s3.update(s2)
print(*s3)

# 3
s4 = s1 & s2
if not s4:
    s4.add('-')
print(*s4)
