import pandas as pd

df = pd.read_csv(r"C:\Users\sathy\Desktop\Git Workspace\Python_programming\DS\Pandas\Sample_Data\SalesJan2020.csv")
country_prod_sales = df.groupby(["Country","Product"]).agg(product_sold_qty = ("Product","count"),Total_sales = ("Price","sum")).reset_index()
country_prod_sales.to_excel(r"C:\Users\sathy\Desktop\Git Workspace\Python_programming\DS\Pandas\Sample_Data\output_file\countrt_product_wisesales_count.xlsx",index = False)

print('Country and product wise summarized outfile generated succesfully!!')

df1 = pd.read_excel(r"C:\Users\sathy\Desktop\Git Workspace\Python_programming\DS\Pandas\Sample_Data\output_file\countrt_product_wisesales_count.xlsx")

print(df1.tail(5))
                            
