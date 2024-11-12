import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/puranjaywadhera/Downloads/cancer.csv")

# Distribution analysis
df['Age'].hist()
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()