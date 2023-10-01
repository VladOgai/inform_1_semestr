import matplotlib.pyplot as plt
import numpy as np


x_vals = list(range(1, 8))
y_vals = [np.random.normal(2 * i, 0.2) for i in x_vals]
least_squares_y = np.interp([0.5, 9], x_vals, y_vals)
plt.plot([0.5, 9], least_squares_y, 'r')
plt.scatter(x_vals, y_vals, marker='x')
plt.show()