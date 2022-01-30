import random
letters_symbols = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

lettersList = random.sample(letters_symbols,10)
#print (lettersList)
print ("".join(lettersList))
