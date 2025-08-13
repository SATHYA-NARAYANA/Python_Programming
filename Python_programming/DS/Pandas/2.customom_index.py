import pandas as pd
nsr_course_fee = ['36k','35k','20k']

#this helps to change default index value to give custom names
nsr = pd.Series(nsr_course_fee,index=['Python Fees:','ETL Fee:','Cloud Fee:'])

print(nsr)
