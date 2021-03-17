import numpy as np
import pandas as pd

# This is the von Frey used
vf2 = [0.38, 0.57, 1.23, 1.83, 3.66, 5.93, 9.13, 13.1]
vf = np.array(vf2)
lvf2 = np.log10(vf2)
# determine difference
kvf2 = lvf2[1:len(lvf2)] - lvf2[0:(len(lvf2) - 1)]
mk2 = np.mean(kvf2)
d = mk2

# get last von Frey tested
# assumes that the starting point for the testing
# is the fourth member of the von Frey group
def get_last(x):
    # x = x.str.lower()
    plc = 3
    for i in range(0, len(x) - 1):
        if x[i] == "o":
            plc += 1
        if x[i] == "x":
            plc -= 1
    return vf2[plc]

filename = input('Please input file name: ')
df = pd.read_csv(filename, index_col=None)
df['Last'] = df['Pattern'].apply(get_last)
table_df = pd.read_excel('new_lookuptable.xlsx', index_col=None)
df_merged = pd.merge(df, table_df, how='left')

# calculates the PWT by taking the log base 10 of the last von Frey used
# and multiplying it but the difference and k
pwtl = np.log10(df_merged['Last']) + d * df_merged['Value']
df_merged['Force'] = 10**pwtl
df_merged.to_excel('df_result.xlsx')
