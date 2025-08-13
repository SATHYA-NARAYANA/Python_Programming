import pandas as pd

df = pd.read_csv(r"F:\PythonProgramming\Pandas\Sample_Data\nsr_customer.csv")

# default print bottom 5 rows
#print(df.tail().to_string(index=False))


# to read and  print bottom 8 rows
print(df.tail(8).to_string(index=False))




