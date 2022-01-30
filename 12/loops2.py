# products = [
# {"name":"bread", "price": 2},
# {"name":"milk", "price": 5},
# {"name":"sugar", "price": 1},
# {"name":"oil", "price": 25},
# {"name":"salt", "price": 1}
# ]

# total = 0
# for i in products:
#     total +=i["price"]
# print(f"Ürünlerin fiyatları toplamı {total}")

# for i in products:
#     if i["price"] < 5:
#         print (f"name : {i['name']}, price : {i['price']}")


text = "I love Python"

# for letter in text:
#     if letter == "e":
#         break
# print (letter)


# text = "I love Python"

# for letter in text:
#     if letter == "e":
#         continue
# print (letter)

# counter=0
# total=0
# while counter < 100:
#     counter +=2
#     total= total + counter
# print (total)

import random
x= random.randint(1, 10)
#print(x)
num= int(input("1-10 dahil bir sayı girin :"))

while num != x :
    if x>num :
        num = int(input("Yukarı :"))
    else:
        num = int(input("Aşağı :"))

print("Tebrikler:)")