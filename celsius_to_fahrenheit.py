def celsius_to_fahrenheit(celsius):
   # complete your function implementation... 
   output = (9 / 5) * celsius + 32

   return output

temperature_celsius = 20
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
print(f"{temperature_celsius}°C is equal to {temperature_fahrenheit}°F")