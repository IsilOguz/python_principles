"""
1-
bir adet student.py dosyası oluşturun
daha önce yazdığımız schoolDB içerisinde tanımladığımız sistemi
Nesne Tabanlı Programlama çerçevesinde yazmak istiyoruz. Bunun için 
bir Student sınıfı oluşturun. (class Student)
Bu Student sınıfını schoolDB deki verilen öğrenci sistematiğine göre
(yani {"sNumber": 101, "name": "Ali", "surname": "Ak","phone": "12345", "wallet": 1000})
tanımlayınız.
"""

class i:
    def __init__(self, sNumber, name, surname, phone, wallet):
        self.sNumber = sNumber
        self.name = name
        self.surname = surname
        self.phone = phone
        self.wallet = wallet

s1 = i (101, "Ali", "Ak", "12345", "1000")
#print (s1.sNumber,s1.name,s1.surname,s1.phone,s1.wallet)
print (s1.__dict__)

s2 = i (102, "Ayşe", "Al", "99999", "500")
#print (s2.sNumber,s2.name,s2.surname,s2.phone,s2.wallet)
print (s2.__dict__)

s3 = i (103, "Zeynep", "Yıldırım", "21222", "900")
#print (s3.sNumber,s3.name,s3.surname,s3.phone,s3.wallet)
print (s3.__dict__)

s4 = i (104, "Mehmet", "Gök", "13579", "400")
#print (s4.sNumber,s4.name,s4.surname,s4.phone,s4.wallet)
print (s4.__dict__)