"""  
Created on Tue oct 18 17:12:00 2021

to separate GW from SW wells/permits using the data 
from uditha's shapefile converted to csv

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd 

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\ECFTX\\"\
                "extractedWellData\\01-rawFiles"
                
os.chdir(dirHome)

dat = pd.read_csv("allECTFXWells.csv")

print(dat['WD_TYPE'].unique())

# filter out wells by well type
datGW = dat[dat['WD_TYPE'] != 'SW']
datSW = dat[dat['WD_TYPE'] == 'SW']

print(datGW['WD_TYPE'].unique())

# save GW wells
datGW.to_csv('ecftxGW_RIBGW.csv')

# save SW wells
datSW.to_csv('ecftxSW.csv')