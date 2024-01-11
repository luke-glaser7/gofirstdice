import itertools
import csv

abcde = 'abcde'
bcdea = 'bcdea'
cdeab = 'cdeab'
deabc = 'deabc'
eabcd = 'eabcd'

letters = [abcde, bcdea, cdeab, deabc, eabcd]

# Instead of getting permutations of the entire strings, we'll get permutations of the indices
permutations = list(itertools.permutations(range(len(letters))))

# Now, we'll use the permutations of indices to construct the new strings
permutated_strings = []
for perm in permutations:
    permutated_string = ''.join(letters[i] for i in perm)
    permutated_strings.append(permutated_string)

combos = list(itertools.combinations(permutated_strings, 3))

# Combine each combination as a new string
combined_strings = [''.join(combo) for combo in combos]

# Make each new string a palindrome
palindromes = [string + string[::-1] for string in combined_strings]

# Save palindromes to a CSV file
csv_file = "palindromes.csv"
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Palindromes"])
    for palindrome in palindromes:
        writer.writerow([palindrome])

print("Palindromes saved to", csv_file)