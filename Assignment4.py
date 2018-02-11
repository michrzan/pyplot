import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

address = "https://www.ncei.noaa.gov/orders/cdo/1207717.csv"
df = pd.read_csv(address)

df = df[["DATE", "HOURLYDRYBULBTEMPC", "HOURLYWindSpeed"]]

%matplotlib notebook
import datetime as dt

def makedate(date):
    return dt.datetime.strptime(date, "%Y-%m-%d %H:%M")
def mph_to_kph(mph):
    try:
        return float(mph) * 1.60934 
    except:
        return np.NaN
    
def wind_top(wind, top):
    return wind if wind > top else np.NaN

df["Date and time"] = df["DATE"].apply(makedate)
df["Wind kph"] = df["HOURLYWindSpeed"].apply(mph_to_kph)

top = np.nanpercentile(df["Wind kph"], 99)
print(top)
df["Wind kph top"] =df["Wind kph"].apply(wind_top, args=(top,))

#print(df)

#print(makedate('2008-01-01 00:37'))

##'%b %d %Y %I:%M%p'
def make_num(x):
    try:
        return float(x)
    except:
        try:
            return float(x[:1])
        except:
            return np.NaN

df["Temperature Celsius"] = df["HOURLYDRYBULBTEMPC"].apply(make_num)


times = [d.to_pydatetime() for d in df["Date and time"]] 
#https://stackoverflow.com/questions/33676608/pandas-type-error-trying-to-plot


fig, ax1 = plt.subplots()
#ax1 = ax2.twinx()

ax1.scatter(times, df["Wind kph top"], color='red', s = 0.5, label='Wind km/h', zorder=1)

ax1.plot(times, df["Temperature Celsius"], linewidth=0.5, color='deepskyblue', label='Temperature [°C]', zorder=2)

plt.gca().set_xlim('2008-01-01', '2018-1-1')

ax1.set_ylim([-45, 60])
#ax2.set_ylim([-40, 40])

#ax2.legend(loc="lower right", fontsize=8)
ax1.legend(loc="lower left", fontsize=8)

plt.xlabel('Date')

plt.title('Temperature and top 1% highest winds in Ann Arbour 2008-2017')
#ax2.set_ylabel('Temperature [°C]')
ax1.set_ylabel('Wind [km/h] \n Temperature  [°C]')
plt.subplots_adjust(bottom=0.25)
