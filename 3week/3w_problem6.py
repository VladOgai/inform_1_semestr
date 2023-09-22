import numpy as np


def mnk_factors(x: np.ndarray, y: np.ndarray) -> tuple:
    matrix = np.vstack([x, np.ones(len(x))]).T
    a, b = np.linalg.lstsq(matrix, y, rcond=None)[0]
    # y = ax + b
    return round(a, 6), round(b, 6)
