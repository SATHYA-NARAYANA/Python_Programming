import pandas as pd

df = pd.read_json(r"F:\PythonProgramming\Pandas\Sample_Data\Companies_DATA1.json")
print(df.to_string(index=False))
