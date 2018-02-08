#def c_to_f(c):
#    if c< -273.15:
#        return "That temperature doesn't make sense!"
#    else:
#        f=c*9/5+32
#        return f
#Please implement a for  loop that iterates through the following temperatures  
#list temperatures=[10,-20,-289,100]  and calls the above c_to_f   function in each iteration. 
#In other words, this time you are using the function to calculate a series of values instead of just one value. 
#
# The expected output: 
#
#50.0
#-4.0
#That temperature doesn't make sense!
#212.0

def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f

temperatures=[10,-20,-289,100]
for temp in temperatures:
    print(c_to_f(temp))
