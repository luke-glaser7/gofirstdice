import csv

def filter_csv_by_value(input_file, output_file, filter_value, column_index):
    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader)  # Read the header row
        filtered_rows = [row for row in reader if row[column_index] == filter_value]

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)  # Write the header row
        writer.writerows(filtered_rows)

# Example usage
input_file = 'count_differences_encoded.csv'
output_file = 'count_differences_encoded_zeros.csv'
filter_value = 0  # Value to filter by
column_index = 7  # Index of the column to filter

filter_csv_by_value(input_file, output_file, filter_value, column_index)
