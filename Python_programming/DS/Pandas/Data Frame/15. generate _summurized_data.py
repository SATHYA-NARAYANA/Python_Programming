import pandas as pd

df = pd.read_csv(r"C:\Users\sathy\Desktop\Git Workspace\Python_programming\DS\Pandas\Sample_Data\SalesJan2020.csv")

country_sales = df.groupby("Country")['Price'].sum().reset_index()
country_sales = country_sales.rename(columns={"Price":"Total_Sales"})

country_sales.to_excel(r"C:\Users\sathy\Desktop\Git Workspace\Python_programming\DS\Pandas\Sample_Data\output_file\salesjan2020_updates.xlsx",index = False)
print("Country wise summarized outfile file generated succesfully")



# by default index value is replaced by country name to override this we use reset_index()
