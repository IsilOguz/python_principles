"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.) 
"""

while True:
    text = input("Enter a string (if you want quit press 'q'):")
    stringList= []
    if text=="q":
        break
    elif text [::-1] == text:
        print(f"{text} is a palindrome string.")
        stringList.append(text)
        print(stringList)

    else:
        print(f"{text} isn't a palindrome string")
        
