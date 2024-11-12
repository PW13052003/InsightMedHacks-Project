import pandas as pd

df = pd.read_csv("/Users/puranjaywadhera/Downloads/cancer.csv")

numeric_data = df.select_dtypes(include=['number'])

# Statistical analysis (Calculate mean, median, standard deviation and range)
mean_value = numeric_data.mean(numeric_only=True)
median_value = numeric_data.median(numeric_only=True)
standard_deviation_value = numeric_data.std(numeric_only=True)
range_value = numeric_data.max() - numeric_data.min()

print("-----")
print("\033[4mMEAN\033[0m:-\n" + str(round(mean_value, 2)))
print("-----")
print("\033[4mMEDIAN\033[0m:-\n" + str(median_value))
print("-----")
print("\033[4mSTANDARD DEVIATION\033[0m:-\n" + str(round(standard_deviation_value, 2)))
print("-----")
print("\033[4mRANGE\033[0m:-\n" + str(round(range_value, 2)))
print("-----")