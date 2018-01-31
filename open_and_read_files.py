# Author: @igorjm
#
# Opening and Reading Files w/ Python

# this commands are used on a shell

>>> file=open("example.txt",'r')

>>> content = file.read()
>>> content = file.readline()
>>> file.seek(0)
>>> content = file.readlines()

>>> print(content)

>>> content=[i.rstrip("\n") for i in content]
>>> content

>>> file.close()