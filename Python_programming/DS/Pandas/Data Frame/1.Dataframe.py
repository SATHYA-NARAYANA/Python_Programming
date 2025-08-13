''' Creating Data Frame using dictionary of list
pd.DataFrame is a class '''

import pandas as pd

nsr_data = {"Course":['DWH','Cloud','Python'],
            "Fees":[35000,20000,36000],
            'Duration':['8 Weeks','4 weeks','10 weeks']
            }
df_nsr_data = pd.DataFrame(nsr_data)
#print(df_nsr_data)
'''Without Index value'''

print(df_nsr_data.to_string(index=False))

'''Both the value of row and colum should be same length i.e 2x2 3x3 else value error occurs'''
