
"""  
Created on Tue Nov 23 15:36:00 2021

get concatenated time series for each pixel
variable is user's choice

@author: Michael Getachew Tadesse

"""
import re
import os 
import pandas as pd 

home_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate\\clipped2MD"

out_dir = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\Climate\\"\
                "pixel_variables"
                
os.chdir(home_dir)

###################
# get unique pixels 
###################
pixel_dat = pd.read_csv('Florida_2000.txt')
pixUnq = pixel_dat['pixel'].unique()


def getTimeSeries(var):
        """  
        var: {'pet', 'ret', 'rs' ,'albedo','rhmax', 
                'rhmin', 'tmax', 'tmin', 'ws'}
        """
    
        for file in os.listdir():
                
                os.chdir(home_dir)
        
                # restrict to 2000 - 2020
                if (int(re.findall(r'\d+', file)[0]) >= 2000) &\
                        (int(re.findall(r'\d+', file)[0]) <= 2017):
                        print(file)
                        dat = pd.read_csv(file)
                        print(dat[['date', 'lat', 'lon', var]])
                        
                        # grouping by pixel
                        dat_group = dat.groupby(['pixel']).agg(list)
                        dat_group.reset_index(inplace = True)
                        
                        # # create empty dataframe for each pixel
                        # df = pd.DataFrame(columns = ['date', 'lat', 'lon', \
                        #                 'pixel', '{}'.format(str(var))])
                                        
                        for px in dat_group['pixel']:
                                newDf = dat_group[dat_group['pixel'] == px]
                                date = pd.DataFrame(newDf['date'].tolist()).T
                                var_dat = pd.DataFrame(newDf['{}'.format(str(var))].tolist()).T
                                
                                new_dat = pd.concat([date, var_dat], axis =1)
                                new_dat.columns = ['date', '{}'.format(str(var))]
                                
                                print(new_dat)                        
                        
                                # create folder for variable
                                os.chdir(out_dir)
                                
                                try:
                                        os.makedirs(str(var))
                                        os.chdir(str(var)) #cd to it after creating it
                                except FileExistsError:
                                        #directory already exists
                                        os.chdir(str(var))
                                        
                                # create folder for file 
                                try:
                                        os.makedirs(file.split('.txt')[0])
                                        os.chdir(file.split('.txt')[0]) 
                                except FileExistsError:
                                        #directory already exists
                                        os.chdir(file.split('.txt')[0])

                                
                                # save pixel variable data
                                new_dat.to_csv(str(px) + ".csv")

getTimeSeries('ret')