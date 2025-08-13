import pandas as pd

df = pd.read_excel("F:/PythonProgramming/Pandas\Sample_Data/Employee_Sample_Data.xlsx")
print(df.to_string(index=False))
