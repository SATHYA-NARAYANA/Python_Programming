import pandas as pd

#df = pd.read_csv(r"F:\PythonProgramming\Pandas\Sample_Data\SalesJan2020.csv")

df = pd.read_csv("F:/PythonProgramming/Pandas/Sample_Data/SalesJan2020.csv")

#print(df)

#display full data if data is less if more it will display top 5 and bottom 5 data !!


#To display full data
x = df.to_string(index=False)

print(x)
