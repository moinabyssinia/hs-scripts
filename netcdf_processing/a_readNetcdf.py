"""
Created on Mon Nov 15 14:19:00 2021

*This script reads NetCDF file and extracts
the requested variables

*browse and locate the desired netcdf file when prompted

# format of ETo in the netcdf file
# (date, latitude, longitude) 

@author: Michael Tadesse

"""

import pandas as pd
from netCDF4 import Dataset
import pandas as pd
from datetime import datetime, timedelta
from tkinter import filedialog as fd


# start the program
def start():
    """ start the program """
    dataset, filename = getFile()

    # prompt user for the variable 
    var_name = input("\n\nEnter the short name for the variable of interest: ")
    print(f"\nYou entered {var_name}.")
    print(f"\nExtracting {var_name} . . .")

    # get requested variables
    lon, lat, date, var = getVariables(dataset, var_name)

    # subset variable
    lat_sub, lon_sub = subset(var, lon, lat)
    
    # get a 2D version of subset variable
    organize(var, var_name, lat_sub, lon_sub, date, filename)

    # done extracting
    print("\nDone Extracting : )  check the folder you saved this script")



def getFile():
    """ asks user for the location of netcdf file 
    """
    netcdf_file = fd.askopenfilename()

    filename = netcdf_file.split("/")[-1]

    g = Dataset(netcdf_file)

    printVariables(g)

    return g, filename



# show the list of all parameters inside the netcdf file
def printVariables(g):
    """  lists all the variables in the netcdf file
    """
    print("-"*95)
    print(g.title)
    print("-"*95)

    print("Variables")
    print("-"*95, "\n")


    for variable in g.variables.keys():

        if (hasattr(g.variables[variable], 'long_name')):
            print(f"{variable:<25}  {g.variables[variable].long_name}")
        else:
            print(f"{variable:<25}  {variable}")



def getVariables(dataset, var):
    """ get essential variables """
    lon = pd.DataFrame(dataset.variables['lon'][:], columns= ['lon'])
    lat = pd.DataFrame(dataset.variables['lat'][:], columns= ['lat'])
    time = pd.DataFrame(dataset.variables['time'][:])
    var = dataset.variables[var]

    # convert days to date
    date = convertTime(time)

    return lon, lat, date, var




def convertTime(time):
    """ 
    adjust time format 
    time - days since 1985-1-1 00:00:00
    """
    getDate = lambda x: datetime(1985, 1, 1) + timedelta(x)
    
    date = pd.DataFrame(list(map(getDate, time[0])), columns= ['date'])

    return date



def subset(var, lon, lat):
    """ 
    subset longitude and latitude using coordinates 
    this needs to allow user to specify coordinates

    lon: [-81.936275, -81.252386]
    lat: [25.847314, 26.581285]

    this particular dataset is organized as time, lat, lon
    """
    lonmin = -81.936275
    lonmax = -81.252386
    latmin = 25.847314
    latmax = 26.581285

    lon_subset = lon[(lon['lon'] >= lonmin) & (lon['lon'] <= lonmax)]
    lat_subset = lat[(lat['lat'] >= latmin) & (lat['lat'] <= latmax)]


    return lat_subset, lon_subset


# organize the requested parameter in time and value format
def organize(var, var_name, lat_sub, lon_sub, date, filename):
    """  
    creates a mesh of the lon and lat subsets
    and subsets the variable with these lon and lat 
    then organizes the variable in such a way that each
    column represents the time series of the variable and 
    each row represents the date
    """

    # dataframe for making the mesh file 
    mesh = pd.DataFrame(columns = ['grid', 'lon', 'lat'])
    var_time_series = pd.DataFrame()
    count = 1

    for lat_ind in range(lat_sub.index[0],lat_sub.index[-1]+1):
        for lon_ind in range(lon_sub.index[0], lon_sub.index[-1]+1):
            # print(lat_ind, lon_ind, lat_sub['lat'][lat_ind], lon_sub['lon'][lon_ind])

            # name grid 
            grid = "g" + str(count)
            newDf = pd.DataFrame([grid, lon_sub['lon'][lon_ind], lat_sub['lat'][lat_ind]]).T 
            newDf.columns = ['grid', 'lon', 'lat']
            mesh = pd.concat([mesh, newDf], axis = 0)

            # build the time series column-wise
            var_time_series[grid] = var[:, lat_ind, lon_ind]

            count += 1

    # save as csv to script directory the grid lon and lat for plotting purposes
    mesh.to_csv("grid_lon_lat_{}.csv".format(filename))

    # concatenate date to time series
    var_time_series = pd.concat([date, var_time_series], axis = 1)

    # save sa csv to script directory
    var_time_series.to_csv("{}_{}.csv".format(var_name, filename))
    
    return var_time_series



""" execute program"""
start()


