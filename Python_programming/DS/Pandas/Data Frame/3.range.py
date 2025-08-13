'''
using Range function to slice
'''

import pandas as pd
data = {"Course": ['Python','DWH','SQL','Hadoop'],
        'Fees': [20000,25000,30000,36000]}
df = pd.DataFrame(data)

x = df.iloc[1:3]

print(x)
