"""  
Created on Tue oct 20 14:27:00 2021

script to add use class - x and y utm coordinates
and counties to the .wel file 

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd 

dirHome = "C:\\Users\\mi292519\\Documents\\hazenStuff\\10202021"
        
dirOut = "C:\\Users\\mi292519\\Documents\\hazenStuff\\10202021\\mergedByYears"

os.chdir(dirHome)

# reading all ECFTX permits
dat = pd.read_csv("ecftx_tr_20190329_stressPeriod_v2.csv")

# reading only the GW sourced permits from udithas shapefile
df = pd.read_csv("ecftxGW_RIBGW.csv")
df.rename(columns={"DISTPRMTST": "name"}, inplace = True)

# get unique years
yrs = dat['year'].unique()

for year in yrs:

    print(year)

    newDat = dat[dat['year'] == year]
    newDf = pd.merge(newDat, df, on="name", how="left")

    newDf = newDf[['X_UTM_m', 'Y_UTM_m', 'layer', 'row', 'columns', 'withdrawal',       
        'name', 'mon', 'year', 'COUNTY', 'USE_CLASS']]

    newDf.columns = ['x_utm_m', 'y_utm_m', 'layer', 'row', 'columns', 'withdrawal',       
       'name', 'mon', 'year', 'county', 'use_class']

    os.chdir(dirOut)
    newDf.to_csv("{}.csv".format(year))

