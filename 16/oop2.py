class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is" , self.name, "I am", self.age, "years old.")

# p1 = Person("Jonh Malkovic", 35)
# p1.myfunc()


# class Student(Person):
#     pass

# x = Student("Ali", 25)
# print(x.name)
# x.myfunc()

class Student(Person):
    def __init__(self, name, age, gradutionyear):
        super().__init__(name,age)
        self.gradutionyear = gradutionyear
    
    def welcome(self):
        print("Welcome", self.name, "to the class of", self.gradutionyear)

stu1 = Student("Ayşe", 15, 2025)
print (stu1.welcome())
print (stu1.name)
print(stu1.gradutionyear)