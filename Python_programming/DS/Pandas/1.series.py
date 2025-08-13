# to_string helps to convert dataframe/series into a formatted string representaion

# i.e to convert row into column.

import pandas

nsr_list = [5,6,12,11,1]


nsr = pandas.Series(nsr_list)

print(nsr.to_string(index=False))

#print(nsr.to_string(index=True))




