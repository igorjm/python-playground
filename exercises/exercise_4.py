# The function that was implemented in the previous exercise checks integer datatypes, but not about floats. 
# So, please expand the conditional block so that floats are counted too.

def string_length(mystring):
    if type(mystring) == int:
        return "Sorry, integers don't have length"
    elif type(mystring) == float:
        return "Sorry, floats don't have length"
    else:
        return len(mystring)

str = input("Please write something: ")
print(string_length(str))