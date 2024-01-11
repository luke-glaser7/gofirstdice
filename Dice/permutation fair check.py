import itertools
from collections import defaultdict

def decipher_alphabetic_string(alphabetic_string):
    dice_set = defaultdict(list)

    for i, letter in enumerate(alphabetic_string):
        dice_set[letter].append(i + 1)

    dice_list = []
    for letter in sorted(dice_set):
        dice_list.append(dice_set[letter])

    return dice_list

#randomly generates a 5d30 palindrome string
import random

def generate_palindrome():
    letters = ['a', 'b', 'c', 'd', 'e']
    is_palindrome = False

    while not is_palindrome:
        string = ''
        for letter in letters:
            string += letter * 15

        # Shuffle the string
        string_list = list(string)
        random.shuffle(string_list)
        shuffled_string = ''.join(string_list)

        # Create the palindrome by concatenating the string and its reverse
        palindrome = shuffled_string + shuffled_string[::-1]

        # Check if the string is a palindrome
        is_palindrome = palindrome == palindrome[::-1]

    return palindrome

# Call the function
result = generate_palindrome()
print("Palindrome String:", result)

#fastpermcheck working!!!
alphabetic_string = result
count = {"" : 1}
dice_set = decipher_alphabetic_string(alphabetic_string)

first_count = None #track the first count encountered

for c in alphabetic_string:
    keys = list(count.keys())  # Create a copy of the keys
    for k in keys:
        if k.count(c) == 0:
            k2 = k + c
            count[k2] = count.get(k2, 0) + count[k]

# Print counts with length 5 and check if they are all equal
is_counts_equal = True
for k, v in count.items():
    if len(k) == 5:
        print(f"Count: {v}, Subsequence: {k}")
        if first_count is None:
            first_count = v
        elif first_count != v:
            is_counts_equal = False

# Check if all counts are equal
if is_counts_equal:
    print("All counts are equal")
else:
    print("Counts are not equal")         

# Print the dice set
for i, dice in enumerate(dice_set):
    print(f"Die {i + 1}: {dice}")
