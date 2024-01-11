from collections import defaultdict

def decipher_alphabetic_string(alphabetic_string):
    dice_set = defaultdict(list)

    for i, letter in enumerate(alphabetic_string):
        dice_set[letter].append(i + 1)

    dice_list = []
    for letter in sorted(dice_set):
        dice_list.append(dice_set[letter])

    return dice_list


# Example usage
alphabetic_string = "abcddcbadbaccabdcbaddabccbaddabcdbaccabdabcddcba"
dice_set = decipher_alphabetic_string(alphabetic_string)

# Print the dice set
for i, dice in enumerate(dice_set):
    print(f"Die {i + 1}: {dice}")

print(dice_set)