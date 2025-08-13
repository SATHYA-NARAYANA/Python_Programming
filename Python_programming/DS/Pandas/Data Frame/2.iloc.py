import pandas as pd
data = {"Course": ['Python','DWH','SQL','Hadoop'],
        'Fees': [20000,25000,30000,36000]}
df_data = pd.DataFrame(data)

#print(df_data)

#single item selection
#print('single item selection:\n')
#print(df_data.iloc[1])

# multiple item selection we use 2 brackets
#print('multiple item selection:\n')
print(df_data.iloc[[1,3]])

# in pandas iloc is used to int based indexing
