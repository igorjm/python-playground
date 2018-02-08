#Create a Python script that generates a new text file which should contain the content of all three text files. 
#So the generated file should have this content:
#Content1 
#Content2 
#Content3 
#In other words, your Python script should merge the three text files. 
#Also, the name of the output file should be the current timestamp. Example:2017-11-01-13-57-39-170965.txt 
#You have some tips in the next lecture and the solution in the lecture after that.

import glob2
import datetime

filenames=glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")