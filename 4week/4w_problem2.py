import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=(10, 5))
fig.subplots_adjust(hspace=0.5)
ax1 = fig.add_subplot(311)
plt.ylabel('Freq')
plt.xlabel('Value')
ax2 = fig.add_subplot(312)
plt.ylabel('Freq')
plt.xlabel('Value')
ax3 = fig.add_subplot(313)
plt.ylabel('Freq')
plt.xlabel('Value')

vals = np.random.normal(0, 40, 1000)
ax1.hist(vals, 50)
ax2.hist(vals, 100)
ax3.hist(vals, 200)

plt.show()