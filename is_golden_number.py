def is_golden_number(n):
    # function implementation ...
    boolean = False  # Initialize the boolean variable

    for a in range(1, n):  # Iterate through all possible values of a
        b = n - a  # Calculate b such that n = a + b
        if b > 0 and (a * b) % 1000 == 0:  # Check the conditions
            boolean = True  # Set to True if conditions are met
            break  # Exit the loop as we found a valid pair

    return boolean

print(is_golden_number(65))  # Expected output: True
print(is_golden_number(70))  # Expected output: True
print(is_golden_number(61))  # Expected output: False