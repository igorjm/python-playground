# Author: @igorjm
#
# Opening and Writing Files w/ Python

# this commands are used on a shell

>>> file = open("example.txt", 'w')
>>> file.write("Line 1\n")
>>> file.write("Line 2\n")
>>> file.close()

>>> array = ["Daenerys", "John", "Cersei"]
>>> file = open("example.txt", 'w')
>>> for item in array:
>>>     file.write(item+"\n")
>>> file.close()