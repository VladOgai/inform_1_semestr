g, s = input().split()
g = int(g)
a = len(s) // g
for i in range(0, len(s), a):
    x = s[i:i+a]
    y = x[::-1]
    s = s.replace(x, y)
print(s)