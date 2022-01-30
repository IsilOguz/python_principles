# my_list=["yesil","mavi","kırmızı","sarı"]
# print(my_list)

# my_list[0]="turuncu"
# print(my_list)

# my_list.insert(2,"fuşya")
# print(my_list)

# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print (car.get("model"))
# car["model"] = "Mondeo"
# print (car)


# my_list=["yesil","mavi","kırmızı","sarı"]
# for i in my_list:
#     print(i)

fruits = {
    "izmir": "üzüm",
    "aydın": "incir",
    "adana": ["karpuz", "mısır"],
    "istanbul": {"bağcılar": ["elma", "armut"], "esenler": "domates", "kadıköy": 10000}
}
"""The elif keyword is pythons way of saying 
"if the previous conditions were not true, then try this condition".


The else keyword catches anything 
which isn't caught by the preceding conditions."""
# for key, value in fruits.items():
#     print(key, "===>", value)

# for key, value in fruits.items():
#     if not isinstance (value, dict):
#        print (key, "===>" , value)
#     else:
#         for key2, value2 in value.items():
#             print (key2, "===>" , value2)
#             print (key, "====>" , key2, "====>", value2)

# a=5
# b=7

# print(a)
# print(b)
# print(a+b)

# userName = "ali"
# password = "12345"

# inputU = input("Kullanıcı adınızı girin :")
# inputP = input("Şifenizi girin :")

# if inputU == userName:
#     if inputP == password:
#        print("Kullanıcı adı ve şifre doğru!")
#        print (f"Hoşdeldin {userName}")
#     else:
#         print ("ŞİFRE HATALI!")
# else:
#     print("KULLANICI ADI HATALI!")

# a=5 
# b=3
#  if a > b:
#      print ("A")
#  else:
#      print("B")

# if a>b: print ("A") else: print ("B")

# x= int(input("x : "))
# y= int(input("y : "))

# if x > y:
#     print ("x is greater than y")
# elif y > x:
#     print ("y is greater than x")
# else:
#     print ("x is equal to y")


# num= int(input("Bir sayı girin :"))
# if num > 0:
#     print (f"{num} sayısı pozitiftir")
# elif num == 0:
#     print (f"{num} sayısı nötrdür.")

# else:
#     print (f"{num} sayısı negatiftir.")