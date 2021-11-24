
"""  
Created on Thu Nov 18 18:15:00 2021

clip USGS tab delimited files to current model domain

@author: Michael Getachew Tadesse

"""
import os 
import pandas as pd 

home_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate\\rawFiles"

out_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate\\clipped2MD"
        
os.chdir(home_dir)

# files = os.listdir()
files = ['Florida_2018.txt']

for file in files:
        
    os.chdir(home_dir)
    
    print(file)

#     dat = pd.read_csv(file, sep='\t', header=None, engine='python') 
    # just for 2018 data - it has header
    dat = pd.read_csv(file, engine='python')
    dat.reset_index(inplace = True)
    dat.drop(['index'], axis = 1, inplace = True)

    print(dat)        

    print("\n", dat.columns)
    # the tab delimited files don't have 'albedo' 
    # columns format for years 1985-2017
#     dat.columns = ['date', 'lat', 'lon', 'pixel', 'pet', 'ret', 'solar',
#                    'rhmax', 'rhmin', 'tmax', 'tmin', 'ws']
    
    # columns format for year 2018
    dat.columns = ['date', 'lat', 'lon', 'pixel', 'pet', 'ret', 'rs' ,'albedo',
                   'rhmax', 'rhmin', 'tmax', 'tmin', 'ws']
    
    ### GLRSTA model domain corners
    # southern lat/lon - [27.11151636372758, -80.58441733981492]
    # western lat/lon - [28.53914861416981, -81.40276960693286] 
    # northern lat/lon - [29.08097244116021, -80.9281679179469]
    # eastern lat/lon - [27.141836016001218, -80.13629440167682] 

    # get only grids that are inside the model domain
    latMin, latMax = 27.11151636372758, 29.08097244116021
    lonMin, lonMax = -81.40276960693286, -80.13629440167682
    
    # convert string to float 
    getFloat = lambda x: float(x)
    
    dat['lat'] = pd.DataFrame(list(map(getFloat, dat['lat'])))
    dat['lon'] = pd.DataFrame(list(map(getFloat, dat['lon'])))
    
    # filter based on grid location
    dat['isInside'] = ( (dat['lat'] >= latMin) & 
                                (dat['lat'] <= latMax) &  
                                        (dat['lon'] >= lonMin) & 
                                                (dat['lon'] <= lonMax) )
    
    
    print(dat)
    
    dat = dat[dat['isInside']]
    
    # save filtered data
    os.chdir(out_dir)
    dat.to_csv(file)
    
    
    
    