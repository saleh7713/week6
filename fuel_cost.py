def fuel_cost(distance_miles):
#     # Constants
    MPG = 50  # Miles per gallon
    LITERS_PER_GALLON = 4.5
    PRICE_PER_LITER = 1.49  # Price in pounds per liter
#     continue function implementation here...
    total_cost = PRICE_PER_LITER * distance_miles * LITERS_PER_GALLON / MPG
    
    return total_cost


print(fuel_cost(50))  # Expected output: 6.705


