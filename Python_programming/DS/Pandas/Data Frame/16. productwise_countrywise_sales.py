import pandas as pd

df = pd.read_csv(r"C:\Users\sathy\Desktop\Git Workspace\Python_programming\DS\Pandas\Sample_Data\SalesJan2020.csv")

country_product_sales = df.groupby("Country","Product")['Price'].sum().reset_index()
country_product_sales = country_product_sales.rename(columns={"Price":"Total_Sales"})

country_product_sales.to_excel(r"C:\Users\sathy\Desktop\Git Workspace\Python_programming\DS\Pandas\Sample_Data\output_file\product_Wise_sales.xlsx",index = False)
print("Country and Product wise summarized outfile file generated succesfully")
