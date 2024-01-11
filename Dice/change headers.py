import csv

filename = 'count_differences1.csv'
row_index = 0  # Index of the row to modify (0-based indexing)
column_index = 3  # Index of the column to modify (0-based indexing)
new_value = 'string'  # Value to replace the cell with

# Read the CSV file and store the rows
rows = []
with open(filename, 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Modify the specific cell
rows[row_index][column_index] = new_value

# Write the modified rows back to the CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
