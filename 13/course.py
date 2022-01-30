# import random

# sayi = random.randint(1,1000000)
# print(sayi)

# import datetime

# now=datetime.datetime.now()
# print(now)

# name= input("What's your name :")
# age = int(input("How old are you :"))
# year = now.year
# print (f"Hello {name.capitalize()} you will be 100 year old in the year :{year-age+100}")

#print("Hello")

# def merhaba():
#     print("merhaba")
#     print("merhaba")
#     print("merhaba")
#     print("merhaba")

# merhaba()



# def merhaba(user):
#     print("merhaba" , user)
#     print("merhaba" , user)
#     print("merhaba" , user)

# merhaba("Ali")
# merhaba("Ayla")
# merhaba("Ayşe")


# def merhaba(user = "Merida"):          
#     print("merhaba" , user)
#     print("merhaba" , user)
#     print("merhaba" , user)

# merhaba("Rapunzel")        #parametre verilince merida yazmaz       

# def multiply(num1,num2):
#     return(num1*num2)

# numberM=multiply(5,10)

# print(numberM)
# def multiply(num1,num2):
#   return(num1*num2)
 
# while True:
#     number1= int(input("the first number :"))
#     number2= int(input("the second number :"))
#     result = multiply(number1,number2)
#     print (f"sonuç {result}.")


def multiply(num1,num2):
  return(num1*num2)
 
while True:
    number1= int(input("the first number(if you want quit press the 'q' button) :"))
    if number1 == "q":
        break
    number2= int(input("the second number (if you want quit press the 'q' button):"))
    if number1 == "q":
        break
    result = multiply(number1,number2)
    print (f"sonuç {result}.")