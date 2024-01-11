import itertools
is_palindrome = False

abcde = 'abcde'
bcdea = 'bcdea'
cdeab = 'cdeab'
deabc = 'deabc'
eabcd = 'eabcd'

letters = [abcde, bcdea, cdeab, deabc, eabcd]

while not is_palindrome:
    string = ''
    string = list(itertools.permutations(letters))
    combos = list(itertools.combinations(string,3))
    print(string)
    # Shuffle the string
    string_list = str(string)
    shuffled_string = ''.join(string_list)
    print(shuffled_string)
    # Create the palindrome by concatenating the string and its reverse
    palindrome = shuffled_string + shuffled_string[::-1]

    # Check if the string is a palindrome
    is_palindrome = palindrome == palindrome[::-1]

#print(palindrome)