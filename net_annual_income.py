def annual_net_income(gross_salary):
    # complete your function implementation here...
    tax_rate = 0

    # Determine tax rate based on gross salary
    if gross_salary >= 45000:
        tax_rate = 50 / 100  # Equivalent to 50%
    elif 30000 <= gross_salary < 45000:
        tax_rate = 30 / 100  # Equivalent to 30%
    else:
        tax_rate = 15 / 100  # Equivalent to 15%

    # Calculate net salary
    net_salary = gross_salary * (1 - tax_rate)

    return net_salary
        

print(annual_net_income(60000))  # Expected output: 25000.0
print(annual_net_income(30000))  # Expected output: 24500.0
print(annual_net_income(20000))  # Expected output: 21250.0


