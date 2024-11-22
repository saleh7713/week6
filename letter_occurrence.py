def letter_occurrence(input_string):
    # complete function implementation...
    count = 0

    # Loop through each character in the string
    for char in input_string:
        # Compare the character with 'a' and 'A'
        if char == 'a' or char == 'A':
            count += 1

    return count

print(letter_occurrence("Amazing"))  # Expected output: 2
print(letter_occurrence("Always aim ambitiously"))  # Expected output: 4