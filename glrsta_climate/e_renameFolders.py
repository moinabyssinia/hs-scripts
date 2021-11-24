
"""  
Created on Tue Nov 24 11:12:00 2021

rename folders to just year and no other
additional string

@author: Michael Getachew Tadesse

"""
import re
import os 

home_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate\\"\
                "pixel_variables\\ret"


def renameIt():
    os.chdir(home_dir)
    
    for file in os.listdir():
        print(file)
        
        # get numbers only 
        new_name = re.findall(r'\d+', file)[0]
        
        # replace folder name
        os.rename(file, new_name)
        
renameIt()