# Create a function that converts Celsius degrees to Fahrenheit. 
# The formula to convert Celsius to Fahrenheit is F = C × 9/5 + 32. 

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

print(convert_celsius_to_fahrenheit(10))