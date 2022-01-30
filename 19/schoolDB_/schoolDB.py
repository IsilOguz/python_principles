from student import Student, s1, s2, s3, s4


class SchoolDB:
    students = [s1,s2,s3,s4]
    def __init__(self, schoolname):
        self.schoolname = schoolname 
    
    def listStu(self):
        for i in self.students:
            #print (Student.__dict__)
            print (i.sNumber, "-", i.name, "-", i.surname, "-",
            i.phone, "-", i.wallet)
     
    def saveStu(self):
            sNumber = int(input("Student Number :"))
            sName = input("Student Name :")
            sSurname = input("Student Surname :")
            sPhone = input("Student Phone Number :")
            wallet = int(input("Wallet Balance :"))
            s5 = Student(sNumber,sName,sSurname,sPhone,wallet)
            self.students.append(s5)

sdb1 = SchoolDB("Atatürk İlkokulu")