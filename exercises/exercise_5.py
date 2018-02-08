# In Exercise 1 it was created a function that converted Celsius degrees to Fahrenheit:

#def cel_to_fahr(c):
#    f = c * 9/5 + 32
#    return f

# Now, the lowest possible temperature that physical matter can reach is -273.15 °C. 
# With that in mind, please improve the function by making it print out a message in case a number lower than -273.15 
# is passed as input when calling the function.

def cel_to_fahr(c):
    if c < -273.15:
        return "Sorry but you reached the lowest possible temperature that physical matter can reach"
    else:
        f = c * 9/5 + 32
    return f

print(cel_to_fahr(-273.4))