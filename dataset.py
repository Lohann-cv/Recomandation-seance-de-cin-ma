import pandas as pd

df = pd.read_csv("diamonds.csv")
print(df.head(10))
df = df[["carat", "cut", "color", "clarity", "price"]]
print(df.head())
