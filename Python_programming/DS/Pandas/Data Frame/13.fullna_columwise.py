# replace null value column wise based on requirement

import pandas as pd
df = pd.read_csv(r"C:\Users\sathy\Desktop\Git Workspace\Python_programming\DS\Pandas\Sample_Data\SalesJan2025.csv")

df['State'] = df['State'].fillna('Karnataka')

df['Country'] = df['Country'].fillna('India')

df.to_csv(r"C:\Users\sathy\Desktop\Git Workspace\Python_programming\DS\Pandas\Sample_Data\output_file\salesJan2025_2.csv",index=False)

print('A new file as been generated succesfully!!')
