# Author: @igorjm
#
# Lists #

list = ["H", 2, "Hello"]

list.append(3)
list.remove(2)

dir(list) # opens all methods inside the list class

print(list)

# Tuples #

t = ("Hello", 3, 4.5)

t[-1]

dit(tuple) # opens all methods inside the tuple class

# Dictionaries #

l = [2,3,4]
d = {"Name:":"John", "Surname":"Snow", "Cities":("Westeros", "Braavos", "Kings Landing")}
d["Name"] # Returns "John"
d["Cities"] # Returns ("Westeros", "Braavos", "Kings Landing")