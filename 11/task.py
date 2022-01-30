"""
1-
Kullanıcıdan üç sınav bilgisi alın,
üç sınavın ortalaması 50 veya büyükse ekrana "Başarılı",
eğer ortalama 50 den küçükse ekrana "Başarısız" yazdırın.
"""

"""
2-
Kullanıcıdan üç sayı alınız ve en büyük sayıyı yazdırınız
"""
"""
3-
öğrenciden üç sınav bilgisi alıp, ortalamasını hesaplatıp aşağıdaki listeye göre
notunu ekrana yazdırın.

0-40 >>> Zayıf
40-50 >>> Geçer
50-70 >>> Orta
70-85 >>> İyi
85-100 >>> Pekiyi

"""

# exam1 = int(input("Sınav notunu girin :"))
# exam2 =  int(input("Sınav notu girin :"))
# exam3 =  int(input("Sınav notu girin :"))
 
# evaluation= ((exam1+exam2+exam3)/3)
# if evaluation<50:
#      print("Başarısız")

# else: 
#     print ("Başarılı")


# num1 = int(input("Bir sayı girin :"))
# num2 = int(input("Bir sayı girin :"))
# num3 = int(input("Bir sayı girin :"))
# if num1>num2 and num1>num3: print(f"{num1} yazdığınız sayıların en büyüğü.")
# elif num2>num1 and num2>num3: print(f"{num2} yazdığınız sayıların en büyüğü")
# else: print(f"{num3} yazdığınız sayıların en büyüğü")


exam1 = int(input("Sınav notunu girin :"))
exam2 =  int(input("Sınav notu girin :"))
exam3 =  int(input("Sınav notu girin :"))
evaluation= ((exam1+exam2+exam3)/3)
if evaluation<40 and evaluation>0:
    print(f"Notun={evaluation} Değerlendirmen:Zayıf")
elif evaluation<50 and evaluation>40:
    print(f"Notun={evaluation} Değerlendirmen:Geçer")

elif evaluation<70 and evaluation>50:
    print(f"Notun={evaluation} Değerlendirmen:Orta")

elif evaluation<85 and evaluation>70:
    print(f"Notun={evaluation} Değerlendirmen:İyi")

else:
    print(f"Notun= {evaluation} Değerlendirmen:Pek İyi")


