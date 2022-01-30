"""
1-)
Input ile isim, eğitim durumu(ilkokul, lise, üniversite) 
ve yaş bilgilerini alalım.
Bu kişi memur olabilir mi yazdıralım. 
==>( Memur olabimek için yaşın 18 ve üzeri olması, eğitimin de lise 
veya üniversite olması gerek.) 
"""
# name = input("Andınızı girin :")
# educationS = input("Eğitim durumunuzu yazınız :(ilkokul/ortaokul/lise)")
# age = int(input("Yaşınızı girin :"))

# if (educationS == "lise" or educationS == "üniversite") and (age >= 18 ):
#     print(f"{name} memur olabilirsin.")

# else:
#     print(f"{name} memur olamazsın.")

# name = input("Andınızı girin :")
# age = int(input("Yaşınızı girin :"))

# if (age >= 18 ):
#     educationS = input("Eğitim durumunuzu yazınız :(ilkokul/ortaokul/lise)")
#     if( educationS == "lise" or educationS == "üniversite"):
#         print(f"{name} memur olabilirsin.")
#     else:
#         print("Memur olamazsın lise ya da üniversite mezunu olmalısın")

# else:
#     print(f"{name} memur olamazsın.")
      

















"""
2-)
Bir ürün listesi oluşturup ürünleri birer dictionary olarak
(aşağıdaki ürün listesini inceleyiniz) ekleyeceğiz:
Bunun için;
Kullanıcıya kaç ürün girmek istediğini sor,
aşağıdaki formata(isim ve fiyat) göre kullanıdan bilgileri alarak
listeye ürünleri ekle,
liste tamamlandığında ürünleri while ile ekrana yazdır.



"""
"""
products = [
                            {"name": "ekmek", "fiyat": 2},
                            {"name": "su", "fiyat": 1},
]
"""
# products = []
# quantity=int(input("How many products do tou want to add? :"))
# counter = 0
# while counter < quantity:
#         name = input("Product name :")
#         price = int(input("Product price :"))
#         products.append({"name" : name , "price" : price})
#         counter +=1

#print(products) 

# for i in products:
#     print(f"Product Name : {i['name']}, Product Price :{i['price']}")

# c= 0
# while c < len(products):
#     print(products[c])
#     c +=1
















"""
3-)
"""

"""
çift sayıları yazdırın,
sayıların toplamını yazdırın,
sayıların kareleri toplamını yazdırın?

"""

nums = [5,7,1,2,3,6,8,12,15,19,4,20]
# for i in nums:
#     if i % 2 == 0:
#        print (i)
   
# total=0
# for i in nums:
#     total +=i
# print(total)

# total=0
# for i in nums:
#      a= i**2
#      total +=a
# print (total)

total=0
for i in nums:
     total +=(i**2) #===> daha kısa!
print (total)

