# Author: @igorjm
#
# Loops

# For
emails = ['me@gmail.com', 'you@hotmail.com', 'they@yahoo.com']
for item in emails:
    if 'gmail' in item:
        print(item)

male_characters = ["John", "Tyrion", "Bran", "Samwell"]
female_characters = ["Cersei", "Daenerys", "Sansa", "Arya"]

for male, female in zip(male_characters, female_characters):
    print(male, female)

    
# While
password = ""
while password != "python":
    password = input("Enter your password: ")
    if password == "python":
        print("You are safe to go!")
    else:
        print("You shall not pass!")

