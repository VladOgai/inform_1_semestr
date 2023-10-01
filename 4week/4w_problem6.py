import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np


dd = pd.read_csv('BTC_data.csv', delimiter=',')
dates = dd['time'].tolist()
cena = dd['close'].tolist()
dates = [i[8:10] + i[4:8] + i[:4] for i in dates]
x = range(1, len(dates) + 1)
z = np.polyfit(x, cena, 15)
p = np.poly1d(z)

figure = plt.figure()
axes = figure.add_subplot(1, 1, 1)
plt.plot(x, cena, label='Non-approximated', color='b')
plt.title('BTC price from 2018 to 2023')
plt.xlabel('Date')
plt.ylabel('Price')
axes.set_xlim(-10, len(dates) + 10)
plt.xticks(range(len(dates)), labels=dates)
axes.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(90))

plt.plot(x, p(x), color='r', label='Approximated')

plt.legend()
plt.show()