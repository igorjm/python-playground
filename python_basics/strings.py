# Author: @igorjm
#
# Strings

c = "Here"

#functions
dir(str) # opens all methods inside the string class
c.replace("e", "i")
c.upper()

#indexing and spliting
c = "Hi There!"

c[0] # Returns: "H"
c[-1] # Returns: "!"
c[0:2] # Returns: "Hi"
c[:2] # Returns: "Hi"
c[3:] # Returns: "There!"
c[-3:-1] # Returns: "re"
c[-3:] # Returns: "re!"