"""  
Created on Tue oct 20 15:00:00 2021

script to concatenate csvs by row

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd 

dirHome = "C:\\Users\\mi292519\\Documents\\hazenStuff\\10202021\\mergedByYears"
        
dirOut = "C:\\Users\\mi292519\\Documents\\hazenStuff\\10202021\\mergedAll"

os.chdir(dirHome)

yrList = os.listdir()

isFirst = True
for yr in yrList:
    print(yr)

    dat = pd.read_csv(yr)
    dat.drop("Unnamed: 0", axis = 1, inplace = True)

    if isFirst:
        df = dat.copy()
        isFirst = False
    else:
        df = pd.concat([df, dat], axis = 0)

print(df)

print(len(df))

os.chdir(dirOut)

df.to_csv("ecftxPermitsAll.csv")