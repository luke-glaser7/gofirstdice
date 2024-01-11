import csv

def is_counts_equal(alphabetic_string):
    count = {"" : 1}
    first_count = None  # track the first count encountered

    for c in alphabetic_string:
        keys = list(count.keys())  # Create a copy of the keys
        for k in keys:
            if k.count(c) == 0:
                k2 = k + c
                count[k2] = count.get(k2, 0) + count[k]

    for k, v in count.items():
        if len(k) == 5:
            if first_count is None:
                first_count = v
            elif first_count != v:
                return False
    return True

# Read alphabetic_strings from palindromes.csv file
csv_file = "palindromes.csv"
output_csv_file = "results.csv"

# Read the contents of the file into a list
with open(csv_file, mode='r', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

# Find the index of the alphabetic_string column
header = data[0]
alphabetic_string_index = header.index("Palindromes")

# Create a list to store results for each line
results = []

# Process each line
for row in data[1:]:  # Skip the header row
    alphabetic_string = row[alphabetic_string_index]
    is_equal = is_counts_equal(alphabetic_string)
    results.append(is_equal)

# Save results to a new CSV file
with open(output_csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header + ["Is_Counts_Equal"])
    for row, result in zip(data[1:], results):  # Skip the header row while writing
        writer.writerow(row + [result])

print("Results saved to", output_csv_file)
