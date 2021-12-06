"""
Created on Mon Dec 06 15:39:00 2021

script to compare ecftx DEM with ecftx well top elevations

@author: Michael Getachew Tadesse

"""

import os 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\MIKE_Modeling_Group - Documents\\"\
    "glrsta-model\\Data\\Elevation\\compare_DEM_wellTop"

os.chdir(dirHome)

dat = pd.read_csv('ecftxWells_DEM_comparison.csv')
allWells = pd.read_csv('allWells_with_watershed_v2.csv')

# get unique well info
getYear = lambda x: x.split('/')[0]


print(allWells.columns)
df = allWells[allWells['date'] == '2004/01/01'][['id', 'layer']]



df.reset_index(inplace=True)
df.drop('index', axis = 1, inplace = True)
df.columns = ['well_id', 'layer']
print(df)
print(len(df['well_id'].unique()))


# # # join dat and allWells on 
dat_merged = pd.merge(dat,df, on="well_id", how="left")

dat_merged = dat_merged[['well_id', 'x', 'y','top', 'bottom', 
                            'dem_value1', 'layer']]

print(dat_merged)
# dat_merged.to_csv("ecftxwellDEM_analysis.csv")

# plot analysis
print(dat_merged['layer'].value_counts())

# plt.figure()
# plt.hist(dat_merged['layer'].value_counts())
# plt.show()


top_wells = dat_merged[dat_merged['layer'] == 1]
top_wells['diff'] = top_wells['dem_value1'] - top_wells['top']
print(top_wells)

sns.set_context('paper', font_scale=1.75)
plt.figure()
plt.hist(top_wells['diff'].abs(), bins = 300)
plt.title('Difference between ECFTX DEM and Top Elevation of ECFTX wells (ft)')
plt.ylabel('Number of Wells')
plt.xlabel('Difference in feet (absolute value)')

plt.show()

print(top_wells['diff'].abs().quantile(0.95))