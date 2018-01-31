#Please modify the code of the previous exercise so that instead of printing out the lines in the terminal, 
#it prints out the length of each line.
#
#Expected output:
#
#4
#5
#6
#8
#10
#11

>>> file = open("fruits.txt", "r")
>>> content = file.readlines()
>>> file.close()
>>> for i in content:
>>>     print(len(i) - 1)