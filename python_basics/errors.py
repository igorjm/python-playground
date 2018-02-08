# Author: @igorjm
#
# Syntax error

int 9  #=> int(9)
print 3  #=> print(3)

#
# Runtime Errors (Exceptions)

a = 1
b = "2"

print(int(2.5) #=> print(int(2.5))
print(a + b) #=> print(str(a) + b) or print(a + float(b))

#
# Exception Handling

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("You are dividing by zero")

print(divide(1,0))
