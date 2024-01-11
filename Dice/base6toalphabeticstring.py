def number_to_letters(number):
    letter_mapping = {
        '1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e'
    }
    
    # Convert the number to a string
    number_str = str(number)
    
    # Map each digit to a corresponding letter
    letters = [letter_mapping[digit] for digit in number_str]
    
    # Join the letters into a single string
    result = ''.join(letters)
    
    return result

# Example usage
number = 313142211355122542355321441311235234241144344432543552253543511225433521451154125334522115345352255345234443441142432532113144123553245221553112241313
letters = number_to_letters(number)
print(letters)  # Output: ab
