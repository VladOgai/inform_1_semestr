import pandas as pd
import matplotlib.pyplot as plt


zu = pd.read_csv('iris_data.csv', delimiter=',')
zlist = zu['Species'].tolist()
zset = list(set(zlist))
zzlist = [zlist.count(i)/len(zlist) for i in zset]
zzlabels = [i for i in zset]

ulist = zu['PetalLengthCm'].tolist()
men = []
rav = []
bol = []
for i in ulist:
    if i >= 1.2:
        men.append(i)
    if 1.2 <= i <= 1.5:
        rav.append(i)
    if i >= 1.5:
        bol.append(i)
a, b, c = len(men), len(rav), len(bol)
uset = [a / (a + b + c), b / (a + b + c), c / (a + b + c)]

fig = plt.figure(figsize=(16, 9))
fig.subplots_adjust(hspace=0.5)
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.set_title('Доли видов ириса в датасете')
ax1.pie(zzlist, labels=zzlabels)
ax2.set_title('Доли ирисов, у которых длина лепестка больше 1.2см, больше 1.2см и меньше 1.5см, больше 1.5см')
ax2.pie(uset, labels=['x>1.2', '1.2<x<1.5', 'x>1.5'])

plt.show()