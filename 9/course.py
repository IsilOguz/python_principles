"""
x = 5


def myFunc():
    global x
    x = 6
    print("x:", x)


myFunc()
print("x:", x)


print(bool(1))
print(bool(0))
print(bool(100))
print(bool(-100))
print(bool("python"))
print(bool(""))
print(bool(["ali", "veli"]))
print(bool([]))

my_list = ["yeşil", "mavi", "kırmızı", "sarı"]
print(my_list)
for i in my_list:
    print(i)

myDict = {"marka": "Opel", "model": "Vectra"}

print(type(myDict))

for i in myDict:
    print(i)

for key, value in myDict.items():
    print(key)
    print(value)

for key, value in myDict.items():
    print(key, " : ", value)

fruits = {
    "izmir": "üzüm",
    "aydın": "incir",
    "adana": ["karpuz", "mısır"],
    "istanbul": {"bağcılar": ["elma", "armut"], "esenler": "domates", "kadıköy": 10000}
}

print(fruits)
print(type(fruits))
a = 0

for key, value in fruits.items():
    if a == 0 or a == 1:
        print(key, "===>", value)
    a += 1


x = {1, 2}

print(type(x))

myset = {"apple", "banana", "cherry", 1, 3}
print(myset)
print(type(myset))

for i in myset:
    print(i)

myList = ["apple", "banana", "cherry", 1, 3, "apple", 1, "apple"]

for i in myList:
    print(i)

myset = {"apple", "banana", "cherry", 1, 3, "apple"}

print(myset)

myList = ["apple", "banana", "cherry", 1, 3, "apple", 1, "apple"]

print("apple" in myList)

myset = {"apple", "banana", "cherry", 1, 3}

print("apple" in myset)
print(1 in myset)

print("t" in "Python")
print("t " in "Python")
print("th" in "Python")

myset = {"apple", "banana", "cherry", 1, 3}

myset.add("milk")
myset.add(999)
myset.add(999.99)
# myset.add([5, 6, 7])
list2 = [5, 6, 7]
# dict2 ={"name":"ayşe", "age": 26}
myset.update(list2)
# myset.update(dict2)
myset.remove(1)
myset.discard(3)
# myset.remove(100)
myset.discard(100)


print(myset)

DATA TYPES
string
numeric ==> int, float, complex

Array
list, tuple
dict, set

"""
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Dictionary is a collection which is ordered* and changeable. No duplicate members.
# Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
"""

text = "merhaba python"
myNumber = 5
my_float = 5.5

# ARRAY
my_list = ["ali", "veli", 1, 3, 3, [1, 2, 3]]
my_list[0] = "ayşe"
my_tuple = ("ali", "veli", 15, 25, 25)
my_dict = {"isim": "ali", "yaş": 25, }
my_set = {"ali", "veli", 15, 26}


PYTHON OPERATORS

Python Arithmetic Operators
x = 5
y = 10
print(x*y)

Python Assignment Operators(Atama operatörleri)
x = 5
x += 5
x = x + 5
print(x)
x *= 5
x *= 10
x = x * 5
print(x)
x /= 3
print(x)

x %= 3
print(x)
"""
# x = 5


# def myFunc():
#     global x
#     x = 6
#     print("x:", x)


# myFunc()
# print("x:", x)


# print(bool(1))
# print(bool(0))
# print(bool(100))
# print(bool(-100))
# print(bool("python"))
# print(bool(""))
# print(bool(["ali", "veli"]))
# print(bool([]))

# my_list = ["yeşil", "mavi", "kırmızı", "sarı"]
# print(my_list)
# for i in my_list:
#     print(i)

# myDict = {"marka": "Opel", "model": "Vectra"}

# print(type(myDict))

# for i in myDict:
#     print(i)

# for key, value in myDict.items():
#     print(key)
#     print(value)

# for key, value in myDict.items():
#     print(key, " : ", value)

# fruits = {
#     "izmir": "üzüm",
#     "aydın": "incir",
#     "adana": ["karpuz", "mısır"],
#     "istanbul": {"bağcılar": ["elma", "armut"], "esenler": "domates", "kadıköy": 10000}
# }

# print(fruits)
# print(type(fruits))
a = 0

# for key, value in fruits.items():
#     if a == 0 or a == 1:
#         print(key, "===>", value)
#     a += 1


# x = {1, 2}

# print(type(x))

# myset = {"apple", "banana", "cherry", 1, 3}
# print(myset)
# print(type(myset))

# for i in myset:
#     print(i)

# myList = ["apple", "banana", "cherry", 1, 3, "apple", 1, "apple"]

# for i in myList:
#     print(i)

# myset = {"apple", "banana", "cherry", 1, 3, "apple"}

# print(myset)

# myList = ["apple", "banana", "cherry", 1, 3, "apple", 1, "apple"]

# print("apple" in myList)

# myset = {"apple", "banana", "cherry", 1, 3}

# print("apple" in myset)
# print(1 in myset)

# print("t" in "Python")
# print("t " in "Python")
# print("th" in "Python")

# myset = {"apple", "banana", "cherry", 1, 3}

# myset.add("milk")
# myset.add(999)
# myset.add(999.99)
# # myset.add([5, 6, 7])
# list2 = [5, 6, 7]
# # dict2 ={"name":"ayşe", "age": 26}
# myset.update(list2)
# # myset.update(dict2)
# myset.remove(1)
# myset.discard(3)
# # myset.remove(100)
# myset.discard(100)


# print(myset)

# DATA TYPES
# string
# numeric ==> int, float, complex

# Array
# list, tuple
# dict, set

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Dictionary is a collection which is ordered* and changeable. No duplicate members.
Set is a collection which is unordered, unchangeable, and unindexed. No duplicate members.
"""

# text = "merhaba python"
# myNumber = 5
# my_float = 5.5

# # ARRAY
# my_list = ["ali", "veli", 1, 3, 3, [1, 2, 3]]
# my_list[0] = "ayşe"
# my_tuple = ("ali", "veli", 15, 25, 25)
# my_dict = {"isim": "ali", "yaş": 25, }
# my_set = {"ali", "veli", 15, 26}


# PYTHON OPERATORS

# Python Arithmetic Operators
# x = 5
# y = 10
# print(x*y)

# Python Assignment Operators(Atama operatörleri)
x = 5
# x += 5
# x = x + 5
# print(x)
# x *= 5
# x *= 10
# x = x * 5
# print(x)
# x /= 3
# print(x)

# x %= 3
# print(x)
"""
Python Comparison Operators  (Karşılaştırma operatörleri)
==  Equal   x == y  
!=  Not equal   x != y     #====> eşit değilse
>   Greater than    x > y   
<   Less than   x < y   
>=  Greater than or equal to    x >= y  
<=  Less than or equal to   x <= y
"""
# x = 10
# y = 10

# if x == y:
#     print("x is equal to y")

# elif x != y:
#     print("x and y are diffent numbers")

# x = 3
# y = 3
# if x >= y:
#     print("y büyük değildir")

"""
Python Logical Operators
and     Returns True if both statements are true    x < 5 and  x < 10   
or  Returns True if one of the statements is true   x < 5 or x < 4  
not Reverse the result, returns False if the result is true not(x < 5 and x < 10)
"""

# x = "ayşe"
# y = 5

# if x == "ali" or y > 3:
#     print("bingo!")
# else:
#     print("olmadı")

x = 3

# if x > 5 and x < 10:
#     print("bingo")

# if x > 5 or x < 10:
#     print("bingo")

# # x = 3
# # if not(x > 5 and x < 10):
# #     print("bingo")

# Python Membership Operators

# myList = [1, 2, 3, 4, 5]

# if 5 in myList:
#     print("bingo")

# if 100 not in myList:
#     print("BİNGOOOOOOOOOOOOOO")


text = "abcdefgh"
if "a " in text:
    print("bingo")


"""
x = 10
y = 10

if x == y:
    print("x is equal to y")

elif x != y:
    print("x and y are diffent numbers")

x = 3
y = 3
if x >= y:
    print("y büyük değildir")

"""
# Python Logical Operators
# and     Returns True if both statements are true    x < 5 and  x < 10   
# or  Returns True if one of the statements is true   x < 5 or x < 4  
# not Reverse the result, returns False if the result is true not(x < 5 and x < 10)
"""

x = "ayşe"
y = 5

if x == "ali" or y > 3:
    print("bingo!")
else:
    print("olmadı")

x = 3

if x > 5 and x < 10:
    print("bingo")

if x > 5 or x < 10:
    print("bingo")

# x = 3
# if not(x > 5 and x < 10):
#     print("bingo")

Python Membership Operators

myList = [1, 2, 3, 4, 5]

if 5 in myList:
    print("bingo")

if 100 not in myList:
    print("BİNGOOOOOOOOOOOOOO")


text = "abcdefgh"
if "a " in text:
    print("bingo")
"""
