import itertools
is_palindrome = False

abcde = 'abcde'
bcdea = 'bcdea'
cdeab = 'cdeab'
deabc = 'deabc'
eabcd = 'eabcd'

letters = [abcde, bcdea, cdeab, deabc, eabcd]

string = ''
string = list(itertools.permutations(letters))
combos = list(itertools.combinations(string,3))
print(string)
