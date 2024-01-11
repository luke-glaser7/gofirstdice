import pandas as pd

# Read the dataset into a DataFrame
data = pd.read_csv('data1.csv')

# Initialize an empty list to store the expanded rows
expanded_rows = []

# Iterate over each row in the DataFrame
for i, row in data.iterrows():
    counts = row['counts']
    subsequence = row['subsequence']
    string = row['string']
    is_counts_equal = row['is_counts_equal']
    num_dice = row['num_dice']
    num_sides = row['num_sides']
    
    # Iterate over the remaining rows to calculate the count differences
    for j in range(i+1, len(data)):
        compared_string = data.at[j, 'string']
        
        # Calculate count difference only if the strings are the same
        if string == compared_string:
            next_counts = data.at[j, 'counts']
            count_difference = next_counts - counts
            compared_subsequence = data.at[j, 'subsequence']
        
            # Append the expanded row with all the necessary columns
            expanded_rows.append([counts, subsequence, compared_subsequence, string, is_counts_equal, num_dice, num_sides, count_difference])

# Create a new DataFrame with the expanded rows
expanded_data = pd.DataFrame(expanded_rows, columns=['counts', 'subsequence', 'compared_subsequence', 'string', 'is_counts_equal', 'num_dice', 'num_sides', 'count_difference'])

# Calculate the number of zeros in count_difference by string
count_zeros = expanded_data.groupby('string')['count_difference'].apply(lambda x: (x == 0).sum()).reset_index(name='num_zeros')

# Merge the count_zeros DataFrame with the expanded_data DataFrame
expanded_data = pd.merge(expanded_data, count_zeros, on='string')

# Write the expanded data to a CSV file
expanded_data.to_csv('count_differences1.csv', index=False)
