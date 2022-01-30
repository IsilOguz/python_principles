 #1-    
# text = "merhaba pytton"
#textteki yanlışı düzeltin

# result = text[:10] +"h"+ text[11:] 
# text = result
# print (text.title())







# # #2-
# """
# "Ali, Ayşe, Fatma, Serdar, Kazım, Eymen, Ezgi" elemanlarıyla "names" listesini oluşturun.

# 1- Listenin ilk elamanı hangisidir, 2. indexinde hangi isim vardır?
# 2- Kaç elemanlıdır yazdırın?
# 3- İlk elemanını Semih yapın
# 4- İlk üç elemanı yazdırın
# 5- İlk dört elemanını yeni bir liste yapın

# """


# #1
# names = ["Ali" , "Ayşe" , "Fatma" , "Serdar" , "Kazım" , "Eymen" , "Ezgi"]
# print (names)
# #2
# print (names[0])
# print (names[2])

# # #3

# result = len(names)
# print (result)

# # #4
# # result = names.insert(0,"Semih")
# # print (names)


# # #5
# print (names[:3])

# #6
# list = names[:4]
# print (list)

countries = ["Turkey", "Germany", "Netherland", "USA", "Russia"]

ages = [20, 35, 13, 20, 42, 15, 20, 54, 20, 23]
"""
1-Yaş listesinden sondaki 23 yaşını siliniz 
2-Yaş listesinin sonuna 80 yaşını ekleyiniz
3-Yaş listesini sıralayın
4-Listenin en genci kaç yaşındadır?
5-En yaşlı ikinci kaç yaşındadır?
6- 20 yaşında kaç kişi var bulun
7-Ülke listesine "France" ekleyin
8-Ülke listesini z-a (ters) sıralayın
9- Kullanıcıdan bir ülke ismi isteyip, ülke listesine ekleyin
10- Yaş listesinin içeriğini silin
"""


# ages.pop()
# ages.remove(20)
# ages.remove(15)
# ages.append(80)
# ages.append("Ali")
# print(ages)
# ages.sort()
# ages.reverse()
# print(min(ages))
# print(max(ages))
# print(ages.count(20))
#print(type(ages.count(20) *5))
countries.append("Frence")
countries.sort()
countries.reverse()

country = input("Bir ülke adı girin : ")
# countries.append(country)

# print(countries)
ages.clear()

print(ages)





print (countries)
#print(ages)