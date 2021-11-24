
"""  
Created on Tue Nov 24 11:24:00 2021

concatenate pixel data for each year

@author: Michael Getachew Tadesse

"""
import re
import os 
import pandas as pd 

home_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate\\"\
                "pixel_variables"

out_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate\\"\
                "pixel_variables\\concatenated"
                


def concatIt(var):
    """  
    var: {'ret', 'pet', etc}
    """
    
    # get unique pixels
    os.chdir(home_dir)
    pixUnq = pd.read_csv("pixels.csv")
    
    # get pixel var folder
    os.chdir(home_dir + "\\{}".format(var))
    years = os.listdir()
    
    # loop through each pixel
    isFirst = True # first year for pixel data
    
    for px in pixUnq['pixels']:
        print(px)
        
        # empty dataframe 
        df = pd.DataFrame()
        
        for yr in years:
            print(yr) 
        
            os.chdir(home_dir + "\\{}".format(var) + "\\{}".format(yr))

            if isFirst:
                df = pd.read_csv(px)
                isFirst = False
            else:
                new_df = pd.read_csv(px)
                df = pd.concat([df, new_df], axis = 0)
        
        # save pixel data
        # allow additional var to be added
        os.chdir(out_dir + "\\ret")
        df.to_csv(px)
        
    
# run code
concatIt('ret')