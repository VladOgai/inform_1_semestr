import numpy as np


def kramer(farr: np.ndarray) -> np.ndarray or None:
    n, m = farr.shape
    if n != m - 1:
        print('Матрица не соответствует СЛАУ')
        return None
    x = farr[0:n, 0:m - 1]
    d = np.linalg.det(x)
    if d == 0:
        print('СЛАУ имеет бесконечное количество решений')
        return None
    b = farr[:, -1]
    dets = []
    for i in range(m - 1):
        xx = x.copy()
        xx[:, i] = b
        dets.append(np.linalg.det(xx))
    return np.array(dets) / d


N, M = map(int, input().split())
x = []
for _ in range(N):
    x.append(list(map(int, input().split())))
x = np.array(x)
print(kramer(x))