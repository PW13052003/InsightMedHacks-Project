import pandas as pd

df = pd.read_csv("/Users/puranjaywadhera/Downloads/cancer.csv")

# Statistical analysis (Calculate mean, median, standard deviation and range)
mean_value = df.mean(numeric_only=True)
median_value = df.median(numeric_only=True)
standard_deviation_value = df.std(numeric_only=True)
range_value = df.max() - df.min()