import os 
import pandas as pd

dirHome = "C:\\Users\\mtadesse\\Hazen and Sawyer\\"\
        "MIKE_Modeling_Group - Documents\\glrsta-model\\Data\\"\
                "LCLU\\sf_sjr_consolidated\\consolidated"
os.chdir(dirHome)

dat = pd.read_csv("missing_MIKE_SHE_code.txt")

print(dat)

print(dat.columns)

print(len(dat[dat['MIKE_SHE_C'] == 0]))

df = pd.DataFrame(dat[dat['MIKE_SHE_C'] == 0]['LCCODE'].unique()).sort_values(0)

for ii in df[0]:
    print(ii)
