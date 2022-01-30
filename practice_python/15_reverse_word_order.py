
text = input("Type a sentence(at least 5 words) :")
reverse = text[::-1]
print (reverse)
reverse2 = " ".join(text.split()[::-1])
print (reverse2)