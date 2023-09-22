import numpy as np


n, m = map(int, input().split())
x, y = 0, 0
dx = 1
dy = 0
spiral = np.array([[0] * m] * n)
for i in range(m * n):
    spiral[y][x] = i + 1
    flagx = x + dx
    flagy = y + dy
    if dx and (flagx < 0 or flagx == m) or dy and (flagy < 0 or flagy == n) or spiral[y + dy][x + dx] != 0:
        dx, dy = -dy, dx
    x += dx
    y += dy
for i in range(n):
    spiral[i] *= i + 1
print(spiral)