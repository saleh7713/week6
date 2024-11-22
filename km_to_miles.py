def km_to_miles(kilometers):
    # complete function implementation here...

    miles_per_kilometer = 0.62

    # Convert kilometers to miles
    miles = kilometers * miles_per_kilometer

    # rounding to 3 decimal places
    miles = int(miles * 1000 + 0.5) / 1000.0

    return miles

print(km_to_miles(120)) 