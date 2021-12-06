
"""  
Created on Thu oct 12 17:23:00 2021

create dfs0 from csv

@author: Michael Getachew Tadesse

"""

import os
from datetime import datetime
from mikecore.DfsFile import DataValueType
from mikeio import Dfs0, Dataset
from mikeio.eum import ItemInfo, EUMType, EUMUnit
import pandas as pd 
from mikeio import Dfs0

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
    "MIKE_Modeling_Group - Documents\\Data\\ET\\glr_ET"

os.chdir(dirHome)

dat = pd.read_csv("stopGapET.csv")
dat['date'] = pd.to_datetime(dat['date'], format = '%m/%d/%Y')


# get the number of days in each month - to get the rate
getNumDays = lambda x: pd.Period(x.strftime('%B-%Y')).days_in_month
numDays = pd.DataFrame(list(map(getNumDays, dat['date'])), columns=['days'])


dat['ET'] = pd.DataFrame(dat['ET']/numDays['days'])
# dat.to_csv("stopGapET_rate.csv")

print(dat)

# organize the columns by changing them to arrays
# but based on columns 
# for the withdrawals - for now use "water volume"

df = []
items = []
for ii in range(1,dat.shape[1]):
    df.append(dat.iloc[:,ii].to_numpy())
    
    ###########################################################
    # make final decision here for EUMUnit *** 
    ###########################################################

    items.append(ItemInfo(dat.columns[ii], EUMType.Evapo_Transpiration, 
                            EUMUnit.inch, 
                                data_value_type= DataValueType.MeanStepBackward))

# generate monthly time from 12/2003 to 12/2014
datTime = pd.date_range(start='08/01/1988', end='12/01/2020', freq='MS')    

'''  
# writing dataframe to dfs0
# use pumping rate for withdrawal
# use meanstepBackward for mean step accumulated
'''
ds = Dataset(data = df, time = datTime, items = items)
print(ds)


# write the dfs0 file


dfs = Dfs0()

dfs.write(filename= "glrET.dfs0", 
        data=ds,
        title="monthly_ET_totals_inches")