import csv

def base10_to_base6(num):
    if num == 0:
        return '0'
    
    digits = []
    
    while num > 0:
        remainder = num % 6
        digits.append(str(remainder))
        num = num // 6
    
    return ''.join(digits[::-1])

# Specify the input and output file paths
input_file = 'condensed_count_differences_encoded.csv'
output_file = 'condensed_count_differences_encoded_basesix.csv'

# Specify the column index to be converted (starting from 0)
column_index = 3

# Open the input and output files
with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    reader = csv.reader(file_in)
    writer = csv.writer(file_out)
    
    for row in reader:
        if len(row) > column_index:
            try:
                # Convert the value in the specified column to base 6
                number = int(row[column_index])
                base6_number = base10_to_base6(number)
                row[column_index] = base6_number
            except ValueError:
                pass  # Skip if the value is not a valid number
        
        # Write the modified row to the output file
        writer.writerow(row)

print("Conversion complete. The output file is generated as 'output.csv'.")
