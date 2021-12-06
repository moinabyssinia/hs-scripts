"""
Created on mon oct 11 16:49:00 2021

script to compare and plot ET data

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
    "MIKE_Modeling_Group - Documents\\Data\\ET"

os.chdir(dirHome)

dat = pd.read_csv("monAggRainfall.csv")
dat['date'] = pd.DataFrame(pd.to_datetime(dat['date']))

# normalize 'ET' result
dat['ET'] = dat['ET']/7


print(dat)

dat = dat.melt(id_vars='date')
sns.set_context("paper", font_scale=2.0)
plt.figure()
sns.lineplot(data = dat, x = 'date', y = 'value', hue = 'variable')
plt.ylabel('Rainfall (inches)')
plt.xlabel('Time')
plt.show()