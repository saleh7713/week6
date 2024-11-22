def find_maximum_difference(a, b):
    # code implementation here...

    # get the first for each
    min_a = a[0]
    max_a = a[0]
    min_b = b[0]
    max_b = b[0]

    # Loop through list a to find the minimum and maximum values
    for num in a:
        if num < min_a:
            min_a = num
        if num > max_a:
            max_a = num

    # Loop through list b to find the minimum and maximum values
    for num in b:
        if num < min_b:
            min_b = num
        if num > max_b:
            max_b = num

    # Calculate the differences manually
    difference1 = max_a - min_b
    difference2 = max_b - min_a

    # Find the larger of the two differences manually
    if difference1 > difference2:
        maximum = difference1
    else:
        maximum = difference2
    
    return maximum


print(find_maximum_difference([1, 5, 600], [100, 7, 3, 29, 39]))  # Expected output: 597
print(find_maximum_difference([1, 5, 600], [100, 7, 3, 602, 39])) # Expected output: 601



