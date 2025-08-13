import pandas as pd

df = pd.read_csv("F:/PythonProgramming/Pandas/Sample_Data/SalesJan2025.csv")

df1 = df.fillna(-1)

df1.to_csv("F:/PythonProgramming/Pandas/Sample_Data/output_file/salesJan2024.csv")

print("A new file has been generated succesfully!!")





