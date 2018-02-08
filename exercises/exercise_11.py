#Please write some code that creates a text file and writes the items of list numbers = [1, 2, 3] to that text file.
#
#The text file content should look like following:
#
#1
#2
#3

>>> numbers = [1, 2, 3]
>>> file = open("file.txt", 'w')
>>> for i in numbers:
>>>     file.write(str(i)+"\n")
>>> file.close()