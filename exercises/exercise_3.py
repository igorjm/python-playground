# def string_length(mystring):
#     return len(mystring)
# Calling the function with a string as the value for the argument mystring  will return the length of that string. 

# However, if an integer is passed as an argument value:

# string_length(10) 

# that would generate an error since the len()  function doesn't work for integers.

# Your duty is to modify the function so that if an integer is passed as an input, 
# the function should output a message like "Sorry integers don't have length".

def string_length(mystring):
    if type(mystring) == int:
        return "Sorry integers don't have length"
    else:
        return len(mystring)

str = input("Please write something: ")
print(string_length(str))