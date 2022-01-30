"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will 
turn 100 years old.
"""



#practice python 1. egzersizi fonksiyon olarak yazdırın.

import datetime

now=datetime.datetime.now()
name= input("What's your name :").capitalize()
while True:
   try:
      age = int(input("How old are you :"))
   except:  
      print("Give me only numbers please")
      continue
   year = now.year

   def my_func():
      print (f"Hello {name.capitalize()} you will be 100 year old in the year :{year-age+100}")

   my_func()

   quit()