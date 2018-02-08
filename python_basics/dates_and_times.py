"""
    This script creates an empty file.
"""
# Importing module datetime
import datetime

filename = datetime.datetime.now()

# Create empty file
def create_file():
    """ This function creates an empty file """
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt", "w") as file:
        file.write("") #Writting empty string

create_file()