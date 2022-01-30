# yorum satırı

"""
Yorum Satırları
Yorum Satırları
Yorum Satırları
"""

# colors = ["yellow", "green", "orange", "brown", "white"]
# counter = 0
# for color in colors:
#     colors[counter] = color+" t-shirt"
#     counter += 1
# print (colors)

customer1= {"costumerNum": 100, "name": "Elif", "surname": "Ak",
            "phone": "123456", "balance": 10000}

customer2= {"costumerNum": 101, "name": "Ali", "surname": "Al", 
            "phone": "123456", "balance": 20000}

# print (costumer1.keys())
# print (costumer1.values())
# print (costumer1.items())

for key,value in customer1:
    print(f"{key},{value}")
