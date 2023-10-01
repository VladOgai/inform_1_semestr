import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


zu = pd.read_csv('iris_data.csv', delimiter=',')
x1list = zu['SepalWidthCm'].tolist()
y1list = zu['SepalLengthCm'].tolist()
dict1 = {}
for i in range(x1list):
    if x1list[i] in dict1.keys():
        dict1[x1list[i]].append(y1list[i])
    else:
        dict1[x1list[i]] = [y1list[i]]
x1 = []
y1 = []
for i in range(dict1.keys()):

x2list = zu['PetalWidthCm'].tolist()
y2list = zu['PetalLengthCm'].tolist()
dict2 = {}
for i in range(x2list):
    if x2list[i] in dict2.keys():
        dict2[x2list[i]].append(y2list[i])
    else:
        dict2[x2list[i]] = [y2list[i]]


fig = plt.figure()
fig.subplots_adjust(hspace=0.5, wspace=0.5)

ax1 = fig.add_subplot(221)
plt.xlabel('Width')
plt.ylabel('Length')
ax2 = fig.add_subplot(222)
plt.xlabel('Width')
plt.ylabel('Length')
ax1.set_title('Sepals')
ax2.set_title('Sepals_mnk')

ax3 = fig.add_subplot(223)
plt.xlabel('Width')
plt.ylabel('Length')
ax4 = fig.add_subplot(224)
plt.xlabel('Width')
plt.ylabel('Length')
ax3.set_title('Petals')
ax4.set_title('Petals_mnk')

ax1.plot(x1list, y1list)

lstsq1 = np.interp([min(x1list) - 0.2, max(x1list) + 0.2], x1list, y1list)
ax2.scatter(x1list, y1list, marker='x')
ax2.plot([min(x1list) - 0.2, max(x1list) + 0.2], lstsq1)
ax2.grid()

ax3.plot(x1list, y1list, label='Petals')

lstsq2 = np.interp([min(x2list) - 0.2, max(x2list) + 0.2], x2list, y2list)
ax4.scatter(x2list, y2list, marker='x')
ax4.plot([min(x2list) - 0.2, max(x2list) + 0.2], lstsq2)
ax4.grid()

plt.show()