"""
Created on mon oct 12 15:33:00 2021

script to prepare rainfall data to fill
gaps in evapotranspiration data

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
    "MIKE_Modeling_Group - Documents\\Data\\ET\\glr_rainfall"

os.chdir(dirHome)

isFirst  = True
for st in os.listdir():
    print(st)
    
    if isFirst:
        newDf = pd.read_csv(st)
        newDf['date'] = pd.to_datetime(newDf['date'])
        dat = newDf
        isFirst = False
    else:
        newDf = pd.read_csv(st)
        newDf['date'] = pd.to_datetime(newDf['date'])
        dat = pd.merge(dat, newDf, on='date', how='outer')
        
dat = dat.sort_values('date')

print(dat)

# dat.to_csv('rainfall_stations.csv')

# aggregate based on month
# print(dat.groupby([pd.Grouper(freq='M'), 'date']).sum())
newSum = dat.resample(rule='M', on='date').sum()
print(newSum)
# newSum.to_csv("monAggRainfall.csv")

# plot comparisons
df = newSum.reset_index()
# print(df.columns)
df = df.melt(id_vars='date')
sns.set_context("paper", font_scale=2.0)
plt.figure()
sns.lineplot(data = df, x = 'date', y = 'value', hue = 'variable')
plt.ylabel('Rainfall (inches)')
plt.xlabel('Time')
plt.show()