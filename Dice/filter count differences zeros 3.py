import csv

def filter_csv_by_value(input_file, output_file, filter_value, column_name):
    with open(input_file, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        filtered_rows = [row for row in reader if row[column_name] == filter_value]

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(filtered_rows)

# Example usage
input_file = 'count_differences1.csv'
output_file = 'count_differences1_zeros.csv'
filter_value = '0'  # Value to filter by
column_name = 'count_difference'  # Name of the column to filter

filter_csv_by_value(input_file, output_file, filter_value, column_name)
