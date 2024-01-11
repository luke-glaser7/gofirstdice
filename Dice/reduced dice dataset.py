import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('count_differences_encoded_zeros.csv')

# Get the last X number of rows
X = 60379  # Set the number of rows you want to extract
Y = 120000
Z = 112860
#last_X_rows = df.tail(Y)
first_X_rows = df.head(X)
#middle_rows = last_X_rows.head(Z)

#combined_rows = pd.concat([middle_rows, first_X_rows])

# Save the last X rows as a new CSV file
first_X_rows.to_csv('condensed_count_differences_encoded_zeros.csv', index=False)
