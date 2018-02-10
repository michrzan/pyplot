import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib notebook

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

ind = np.arange(4)
means = df.mean(axis=1)
std = df.std(axis=1)
yerr = 1.96 * std / len(df.columns)**0.5

plt.figure()
my_bars = plt.bar(ind, means)          
plt.errorbar(ind, means, yerr = yerr, capsize=20, fmt=',', color='k')
plt.xticks(ind, ('1992', '1993', '1994', '1995'))
plt.gca().set_ylim(0, 5.25*10**4)
plt.gca().set_title('Random data for years 1992-1995:\n')
my_line = plt.axhline(y=0, color='k')     


def onclick(event):
    y = event.ydata
    for bar_num in range(4):
        if y < means.iloc[bar_num] - yerr.iloc[bar_num]:
            col = 'r' 
        elif y > means.iloc[bar_num] + yerr.iloc[bar_num]:
            col = 'b' 
        else:
            col = 'g'
        my_bars[bar_num].set_color(col)
    my_line.set_ydata(y)
    plt.gca().set_title('Random data for years 1992-1995:\n' + 'line at: ' + str(int(y)))


plt.gcf().canvas.mpl_connect('button_press_event', onclick)
