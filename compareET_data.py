"""
Created on mon oct 11 16:06:00 2021

script to compare and plot ET data

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

dirHome = "C:\\Users\\mtadesse\\"\
        "Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
                "glrsta-model\\GLRSTA_Ideal1000\\GLRSTA_Ideal1000\\MSHE\\INPUT_FILES\\ET"

os.chdir(dirHome)

dat = pd.read_csv("etData.csv")

print(dat)

# convert mm to inches
"""  
JDWX and SVWX change to inches
1 mm = 0.03937008 inch
"""

print(dat['station'].unique())

station = dat['station'].unique()

isFirst = True
for st in station:
    print(st)
    
    if(isFirst):
        df = dat[dat['station'] == st]
        df = df[['timestamp', 'value']]
        df.columns = ['timestamp', st]
        
        if ((st == 'JDWX') | (st == 'SVWX')):
            df[st] = df[st]*0.03937008
        
        isFirst = False
    else:
        newDf = dat[dat['station'] == st]
        newDf = newDf[['timestamp', 'value']]
        newDf.columns = ['timestamp', st]
        
        if ((st == 'JDWX') | (st == 'SVWX')):
            newDf[st] = newDf[st]*0.03937008
            
        df = pd.merge(df, newDf, on='timestamp', how='outer')

# df.to_csv('allMergedET.csv')

df['timestamp'] = pd.to_datetime(df['timestamp'])

print(df.describe())

df = df.melt(id_vars='timestamp')
print(df)


# plot and compare
sns.set_context("paper", font_scale=2.0)
plt.figure()
sns.lineplot(data = df, x = 'timestamp', y = 'value', hue = 'variable')
plt.ylabel('ET (inches)')
plt.xlabel('Time')
plt.show()