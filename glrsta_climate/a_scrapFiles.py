
"""  
Created on Tue Nov 16 17:24:00 2021

web scrap csv files from a website

@author: Michael Getachew Tadesse

"""

import os
import requests 

out_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate"

years = list(range(1985,2018))

os.chdir(out_dir)

for yr in years:
    print(yr)
    url = "https://fl.water.usgs.gov/et/data/{}/Florida_{}.zip".format(yr,yr)
    r = requests.get(url, allow_redirects=True)
    
    # get names for files
    fileName = "Florida_"+str(yr)+".zip"
    
    # save file 
    with open(fileName, "wb") as f:
        f.write(r.content)
    

