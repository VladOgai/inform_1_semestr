import matplotlib.pyplot as plt
import numpy as np


x_vals = [1, 2, 3, 4, 5]
plt.plot(x_vals, label='An awesome line')
plt.ylabel('The y-axis label')
plt.xlabel("The x-axis label")
plt.title("THE TITLE")
plt.legend()
plt.savefig('mygraph.pdf', dpi=1200)
plt.show()