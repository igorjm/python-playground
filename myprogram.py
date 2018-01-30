# Author: @igorjm
#
# running program

def age_foo(age):
    new_age = age + 50
    return new_age

age = int(input("Enter your age: "))

if age < 150:
    print(age_foo(age))
else:
    print("How is that possible?")

#print(age_foo(age))
#print("You will be " + age_foo(age) + " years old in 50 years from now")