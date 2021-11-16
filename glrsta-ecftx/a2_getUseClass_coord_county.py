"""  
Created on Tue oct 19 15:24:00 2021

script to add use class - x and y utm coordinates
and counties to the .wel file 

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd 

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
        "ECFTX\\extractedWellData\\01-rawFiles"
        
os.chdir(dirHome)

####################
# load original file
#################### 
dat = pd.read_csv("ecftx_tr_20190329_stressPeriod_v2.csv")

#####################################
# add x, y, county, use_class columns
#####################################
dat['x'] = 'nan'
dat['y'] = 'nan'
dat['county'] = 'nan'
dat['use_class'] = 'nan'

print(dat)

print(len(dat['name'].unique()))
print(dat['name'].unique())

# load GW permits obtained from Uditha's shapefile
df = pd.read_csv("ecftxGW_RIBGW.csv")
print(df)

unqPermit = dat['name'].unique()

for permit in unqPermit:
    print(permit)
    
    # get the values from the shapefile file
    use_class = df[df['DISTPRMTST'] == permit]['USE_CLASS']
    
    dat.loc[(dat.name == permit), 'use_class'] = use_class
    
print(dat)

dat.to_csv("testAllEctfxPermits.csv")