import csv

def letter_to_number(string):
    result = 0

    for char in string:
        if char.isalpha():
            number = ord(char) - ord('a') + 1
            result = result * 10 + number

    return result

def base6_to_base10(number):
    number = str(number)
    base10 = 0
    power = 0

    for digit in number[::-1]:
        base10 += int(digit) * (6 ** power)
        power += 1

    return base10

# Example usage
filename = 'count_differences1.csv'
column_index = 3  # Index of the column to convert, assuming 0-based indexing

rows = []  # To store the modified rows

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if column_index < len(row):
            input_string = row[column_index]
            output_number = letter_to_number(input_string)
            output_baseten_number = base6_to_base10(output_number)
            
            row[column_index] = str(output_baseten_number)  # Replace the input string with the new number
            rows.append(row)

# Write the modified rows back to the CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
