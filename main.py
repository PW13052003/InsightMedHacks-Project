# Contributor(s): Puranjay Wadhera
# Email: pw425@drexel.edu
# Dataset used: cancer.csv
    # Source: https://www.kaggle.com/datasets
# Originally submitted to: Devpost (InsightMed Hacks Hackathon)

# Import the necessary modules
    # pandas is being used to read data
    # matplotlib is being used to plot graphs
    # seaborn is being used for finding correlations
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the file
df = pd.read_csv("/Users/puranjaywadhera/Downloads/cancer.csv")

# For statistical analysis and plotting graphs, we will only consider data attributes with a numerical data type
numeric_data = df.select_dtypes(include=['number'])

# Statistical analysis (Calculate mean, median, standard deviation and range)
mean_value = numeric_data.mean(numeric_only=True)
median_value = numeric_data.median(numeric_only=True)
standard_deviation_value = numeric_data.std(numeric_only=True)
range_value = numeric_data.max() - numeric_data.min()
# Print findings
print("-----")
print("\033[4mMEAN\033[0m:-\n" + str(round(mean_value, 2)))
print("-----")
print("\033[4mMEDIAN\033[0m:-\n" + str(median_value))
print("-----")
print("\033[4mSTANDARD DEVIATION\033[0m:-\n" + str(round(standard_deviation_value, 2)))
print("-----")
print("\033[4mRANGE\033[0m:-\n" + str(round(range_value, 2)))
print("-----")

# Plot histograms for each column
for column in numeric_data.columns:
    plt.figure(figsize=(8, 6))  # Create a new figure for each plot
    plt.hist(numeric_data[column], bins=30, edgecolor='black')  # Adjust bins as needed
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Determine the correlations
correlation_matrix = numeric_data.corr()

# Plot the correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", cbar=True)
plt.title("Correlation Matrix of Numerical Columns")
plt.show()