import pandas as pd
df = pd.read_csv(r"C:\Users\sathy\Desktop\Git Workspace\Python_programming\DS\Pandas\Sample_Data\customer.csv")
df1 = df.drop_duplicates()

df1.to_csv(r"C:\Users\sathy\Desktop\Git Workspace\Python_programming\DS\Pandas\Sample_Data\output_file\customer_report.csv", \
           index = False)

print("Duplicate data is removed and exported succesfully!!")

