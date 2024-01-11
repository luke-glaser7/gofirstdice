import itertools
import csv

palindromes = []
abcde = ['abcde']
bcdea = ['bcdea']
cdeab = ['cdeab']
deabc = ['deabc']
eabcd = ['eabcd']

letters = [abcde, bcdea, cdeab, deabc, eabcd]

# Generate all possible combinations of the letters
combinations = list(itertools.permutations(letters*3))

# Check each combination for palindromes
for combination in combinations:
    # Create a palindrome by appending the reverse of the combination
    palindrome = ''.join(combination) + ''.join(combination[::-1])
    palindromes.append(palindrome)
    print(palindrome)

# Save palindromes to a CSV file
filename = 'palindromes.csv'
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Palindrome'])
    writer.writerows([[p] for p in palindromes])

print(f"Palindromes saved to {filename}.")

# Print the list of palindromes
#for palindrome in palindromes:
#    print(palindrome)
