def base10_to_base6(num):
    if num == 0:
        return '0'
    
    digits = []
    
    while num > 0:
        remainder = num % 6
        digits.append(str(remainder))
        num = num // 6
    
    return ''.join(digits[::-1])

number = 42
base6_number = base10_to_base6(number)
print(base6_number)  # Output: 120