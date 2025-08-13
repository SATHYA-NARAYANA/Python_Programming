import pandas as pd

try:
    df = pd.read_csv(r"F:\PythonProgramming\Pandas\Sample_Data\nsr_customer.csv")
    print(df.to_string(index=False))

except FileNotFoundError:
    print("Message: File not found or file does not exists")
    
    
