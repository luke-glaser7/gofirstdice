import csv

def filter_csv_by_value(input_file, output_file, filter_value, column_index, has_header=True):
    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        headers = next(reader) if has_header else None
        filtered_rows = [row for row in reader if row[column_index] == filter_value]

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if has_header:
            writer.writerow(headers)
        writer.writerows(filtered_rows)

# Example usage
input_file = 'count_differences_encoded.csv'
output_file = 'count_differences_encoded_zeros.csv'
filter_value = 0  # Value to filter by
column_index = 2  # Index of the column to filter
has_header = True  # Set this to False if the CSV file doesn't have a header row

filter_csv_by_value(input_file, output_file, filter_value, column_index, has_header)

