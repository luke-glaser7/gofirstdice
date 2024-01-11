import pandas as pd
import seaborn as sns

# Read the CSV file
data = pd.read_csv('count_differences_encoded_zeros.csv')

# Extract the relevant columns
columns = ['counts', 'subsequence', 'compared_subsequence', 'is_counts_equal', 'num_dice', 'num_sides', 'count_difference']
subset = data[columns]

# Create a pairplot
sns.pairplot(subset)
sns.figure.show()