"""
Middle letter
Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return ""
"""

def mid(a):
    if len(a) % 2 == 1:
        return a[len(a) // 2]

    else:
        return ""