"""
Writing short code
Define a function named convert that takes a list of numbers as its 
only parameter and returns a list of each number converted to a string.
For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
What makes this tricky is that your function body must only contain a 
single line of code.
"""

def convert(a):
    newList = []
    for i in a:
        newList.append(str(i))
    return newList

# short

def convert(a):
    return list(map(str,a))

# or

def convert(ns):
    return [str(n) for n in ns]