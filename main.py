import pandas as pd

df = pd.read_csv("/Users/puranjaywadhera/Downloads/cancer.csv")
missing = df.isnull().sum()
print(missing)