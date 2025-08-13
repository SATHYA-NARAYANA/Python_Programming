import pandas as pd

df = pd.read_csv("F:/PythonProgramming/Pandas/Sample_Data/SalesJan2024.csv")

df1 = df.dropna()

print(df1.to_string(index=False))




