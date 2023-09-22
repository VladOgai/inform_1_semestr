import numpy as np
import random


def mnk_factors(x: np.ndarray, y: np.ndarray) -> tuple:
    matrix = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(matrix, y, rcond=None)[0]
    # y = ax + b
    return round(a, 6), round(b, 6)


def rand_znach(n: int) -> tuple:
    xx = np.array([i for i in range(1, n + 1)])
    res = np.array([random.gauss(i, 2) for i in range(1, n + 1)])
    return xx, res


N = int(input())
print(mnk_factors(*rand_znach(N)))
