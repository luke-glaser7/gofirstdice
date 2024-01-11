import csv

filename = 'count_differences_encoded_zeros.csv'
x = 5  # Number of rows to print

with open(filename, 'r') as file:
    reader = csv.reader(file)
    
    # Iterate over the rows and print the first X rows
    for i, row in enumerate(reader):
        if i >= x:
            break
        
        print(row)
