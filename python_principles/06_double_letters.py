"""
Double letters
The goal of this challenge is to analyze a string to check if it contains two of thesame letter in a row.
For example, the string "hello" has l twice in a row, while the string "nono" 
does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter.
The parameter is a string.
Your function must return True if there are two identical letters in a row in 
the string, and False otherwise.
"""

# def double_letters(a):
#     letter1 = ""
#     for i in a :
#         if i == letter1:
#             return True
#         letter1 = i
#     return False
# print (double_letters("numan"))

def double_letters(a):
    a = a.lower()
    for i in range(len(a)-1):
        letter1 = a[i]
        letter2 = a[i+1]
        if letter1 == letter2:
            return True
        
    return False 

