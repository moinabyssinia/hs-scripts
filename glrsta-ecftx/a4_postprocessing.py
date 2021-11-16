"""  
Created on Tue oct 20 15:00:00 2021

script to concatenate csvs by row

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd 

dirHome = "C:\\Users\\mi292519\\Documents\\hazenStuff\\10202021\\mergedAll"
        
# dirOut = "C:\\Users\\mi292519\\Documents\\hazenStuff\\10202021\\mergedAll"

os.chdir(dirHome)

dat = pd.read_csv("ecftxPermitsAll.csv")
# print(dat)

totalByYear = pd.DataFrame(dat.groupby(['year'])['withdrawal'].sum())
totalByUse = pd.DataFrame(dat.groupby(['use_class'])['withdrawal'].sum())
totalByCounty = pd.DataFrame(dat.groupby(['county'])['withdrawal'].sum())

# melting with multiple columns
useYear = pd.DataFrame(dat.groupby(['use_class','year'])['withdrawal'].sum())

print(totalByYear)
print(totalByUse)
print(totalByCounty)
print(useYear)

totalByYear.to_csv("totalByYear.csv")
totalByUse.to_csv("totalByUse.csv")
totalByCounty.to_csv("totalByCounty.csv")
useYear.to_csv("useYear.csv")