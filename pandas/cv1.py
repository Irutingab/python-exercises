import pandas as pd

df = pd.read_csv('data.csv')

print(df.duplicated())
duplicates = df[df.duplicated()]
print("Duplicate Rows:")
print(duplicates)
