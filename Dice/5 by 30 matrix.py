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
