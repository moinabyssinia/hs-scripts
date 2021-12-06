"""
Created on Wed Sep 01 17:03:00 2021

script to read .mdb soil files

@author: Michael Getachew Tadesse

"""

import os 
from meza import io


os.chdir("C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\Data\\soilData\\FL061")
print(os.listdir())


records = io.read('soildb_FL_2003.mdb') # only file path, no file objects

print(next(records))