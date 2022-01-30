
#1-
"""
"https://pythonprinciples.com/challenges/Capital-indexes/"
adresindeki görevi yapınız. (Aşağıda problemin ingilizce ile Türkçe çevirisi verilmiştir. Önce ingilizcede kendinizi zorlayarak yapmaya çalışın. Sonra Türkçesine bakabilirsiniz)
"""
"""
Capital indexes
Write a function named capital_indexes.
The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in 
the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

"""
capital_indexes  adında bir fonksiyon yazın.
Bu fonksiyon bir adet parametre alsın, parametrenin türü string olsun.
Fonksiyon bir liste dönsün, bu listede parametre olarak verdiğimiz string 
içindeki büyük harflerin indeksleri olsun.

Mesela,
capital_indexes("HeLlO")
fonksiyonunu çağırdığımızda, [0, 2, 4] listesi dönmeli.

"""
# def capital_indexes(a):
#     capitalIndexList = []
#     counter = 0
#     for i in a:
#         if i.isupper():
#             capitalIndexList.append(counter)
#         counter += 1
#     print(capitalIndexList)
# capital_indexes("He<LlO")


"""

2-
"https://pythonprinciples.com/challenges/Middle-letter/"
adresindeki görevi yapınız. (Aşağıda problemin ingilizce ile Türkçe çevirisi verilmiştir. Önce ingilizcede kendinizi zorlayarak yapmaya çalışın. Sonra Türkçesine bakabilirsiniz)

"""
"""
Middle letter
Write a function named mid that takes a string as its parameter. 
Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return ""
"""
"""
mid() isimli bir fonksiyon yazın. 
parametre olarak bir string alsın.
fonksiyon çalıştırılınca ortadaki harfi dönmeli.
Eğer orta karakter yoksa, yani string çift harfliyse, fonksiyon boş string dönmeli.

Mesela mid("abc") fonksiyonu "b" dönmeli,
mid("aaaa") fonksiyonu "" dönmeli.
"""

def mid(a):
    if len(a) % 2 == 1:
        return a[len(a) // 2]

    else:
        return ""








#3-
"""
"https://pythonprinciples.com/challenges/Online-status/"
adresindeki görevi yapınız. (Aşağıda problemin ingilizce ile Türkçe çevirisi verilmiştir. Önce ingilizcede kendinizi zorlayarak yapmaya çalışın. Sonra Türkçesine bakabilirsiniz)
"""
"""
Online status
The aim of this challenge is, given a dictionary of people's online status,
to count the number of people who are online.
For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.
Write a function named online_count that takes one parameter. 
The parameter is a dictionary that maps from strings of names to the string 
"online" or "offline", as seen above.
Your function should return the number of people who are online.
"""
"""
Bu bölümde size kişilerin online durumlarını gösteren bir dictionary verilecektir.
Ve sizden toplamda online olan kişilerin sayısı istenecektir.
Mesela aşağıdaki dictionary i inceleyin:
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
bu örnek için online kişi sayısı 2 dir.
online_count adında tek parametre alan bir fonksiyon yazın.
Parametre yukarıdaki gibi isimlere göre "online" veya "offline" olma durumlarını gösterecektir.
Sizin yazdığınız fonksiyon da, toplam "online" kişi sayısını dönmelidir.
"""

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
def online_count(a):
    onlineCount = []
    for i,j in a.items():
        if j == "online":
            onlineCount.append(i)
    print(len(onlineCount))
online_count(statuses)





