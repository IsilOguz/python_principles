
"""
# 1- my_text değişkeninden "Python" ifadesini çekin

# 2- my_text değişkeninden "today" ifadesini çekin

# 3- Bütün ifadeyi tersten yazdırın

# 4- Baştaki 10 karakteri yazdırın

# 5- Sondaki 10 karakteri yazdırın
"""



my_text = "We learn Python variables and Data Types today."

# 1.
my_text = "We learn Python variables and Data Types today."
print (my_text[9:15])

# 2.
lenght = (len(my_text))
word= my_text[lenght-6 : lenght-1]
print (word)


# 3.
# print (len(my_text))
print (my_text [::-1])

# 4.
print (my_text[0:10])

#5 
print (my_text[-10:])








"""
Dairenin Alanı      : pi sayısı * yarıçapın karesi
Dairenin Çevresi    : 2 * pi sayısı * yarıçap

Kullanıcıdan yarıçapı isteyiniz, kullanıcının girdiği yarıçap verisine göre
dairenin alanını ve çevresini hesaplayıp ekrana yazdırınız. (pi sayısı: 3.14)

"""

yaricap= input ("Dairenizin yarı çapının değeri :")
yaricap = float (yaricap)
print ("Dairenizin Alanı :" + str(3.14 * yaricap ** 2))
print ("Dairenizin Çevresi :" + str(2 * 3.14 * yaricap))