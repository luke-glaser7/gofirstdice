def letter_to_number(string):
    #string = string.lower()  # Convert the string to lowercase to handle uppercase letters as well
    result = 0
    
    for char in string:
        if char.isalpha():
            number = ord(char) - ord('a') + 1
            result = result * 10 + number  # Treat the string as base 10 to handle multiple characters
            
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
input_string = "abcdeabcde"
output_number = letter_to_number(input_string)
output_baseten_number = base6_to_base10(output_number)
print(output_number)
print(output_baseten_number)
