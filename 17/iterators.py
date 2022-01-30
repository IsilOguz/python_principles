# def my_func(*kids):
#     print("The youngest child is " + kids[2])
    
# my_func("Marthew", "Dean", "Nezuko", "Jimmy")

# def my_func(**kid):
#     print("His only child is " + kid['fname'])
    
# my_func(fname='Eri' , lname='Chan')


#oop nesne tabenlı programlama :)


#{"key":1, "value":"x"}

class Magazine:
    def __init__(self, title):
        self.title = title
    


class Newspaper:
    def __init__(self, title):
        self.title = title

m1 = Magazine ("Nokta Dergisi")
m2 = Magazine ("Vogue")

n1 = Newspaper ("Hürriyet Gazetesi")
n2 = Newspaper ("Sabah Gazetesi")

print (m1.title)
print (m2.title)
print (n1.title)
print (n2.title)