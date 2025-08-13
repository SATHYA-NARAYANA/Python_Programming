# how to access series by its index number or by its custome label by user
import pandas as pd

course_fee = [36000,35000,20000]
nsr = pd.Series(course_fee)
#print(nsr[1])


nsr = pd.Series(course_fee,index=['Python Fees:','ETL Fee:','Cloud Fee:'])
print(nsr["Python Fees:"])
