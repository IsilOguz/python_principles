"""
Kişiden kilosunu ve boyunu(cm olarak örnek 165 cm) isteyiniz. Kişinin kilo-boy endeksini hesaplatıp
aşağıdaki tabloya göre durumunu yazdırın. Kilo boy endeksi:( kilo * 10000 / boyun karesi(cm) )

0-18.4 ===>zayıf
18.5-24.9 ===> Normal
25.0-29.9 ===> Kilolu
30.0-34.9 ===> Şişman(Obez)
"""
# isim=input("Adınızı girin :")
# kilo = int(input("Kilonuzu girin :"))
# boy = int(input("Boyunuzu girin :"))
# endeks= ((kilo*10000)/(boy**2))
# if endeks <= 18.4 and endeks > 0: print("Zayıf")
# elif endeks <= 24.9 and endeks > 18.5: print ("Normal")
# elif endeks  <= 29.9 and endeks > 25.0: print ("Kilolu")
# else : print("Şişman(Obez)")











"""
1-10 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
"""
import random
num = random.randint(1, 10)
#print(num)
can = int(input("Kaç kerede bilebilirsin? :"))
hak = can
counter = 0
while hak > 0:
 hak -= 1
 counter += 1
 userN = int(input("Bir ve on arası bir sayı girin(bir ve on dahil) :"))
 if userN == num :
    print(f"Tebrikler sayı, {num} idi. {counter}. deneyişinde bildin. Puanın {100 - ((100/can)*(counter-1))}")
    break

 elif num > userN:
     print("Yukarı ")
     
 elif num < userN:
     print ("Aşağı ")
     
 if hak == 0: 
    print (f"Canın kalmadı! Kaybettin.Sayı {num} idi")
    break

print("Oyundan çıkılıyor...")


 
  


   
     
