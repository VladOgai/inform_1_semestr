n = int(input())
fibs = [0 for _ in range(n)]

fibs[0] = 0
fibs[1] = 1
for i in range (2, n):
    fibs[i] = fibs[i - 1] + fibs[i - 2]

print(fibs[n - 1])