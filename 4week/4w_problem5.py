import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker


dd = pd.read_csv('BTC_data.csv', delimiter=',')
dates = dd['time'].tolist()
cena = dd['close'].tolist()
dates = [i[8:10] + i[4:8] + i[:4] for i in dates]

figure = plt.figure()
axes = figure.add_subplot(1, 1, 1)
plt.plot(range(1, len(dates) + 1), cena)
plt.title('BTC price from 2018 to 2023')
plt.xlabel('Date')
plt.ylabel('Price')
axes.set_xlim(-10, len(dates) + 10)
plt.xticks(range(len(dates)), labels=dates)
axes.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(90))
# шаг +-3 месяца
# я вообще хз как это работает, главное что работает
plt.show()
