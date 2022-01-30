class Book:
    def __init__(self, title, pageCount, author, price):
        self.title = title
        self.pageCount = pageCount
        self.author = author
        self.price = price

    def setdiscount(self, amount):
        self.amount = amount

    def getprice(self):
        # if hasattr(self, amount):
        #     return self.price - (self.price * self.amount)
        # else:
        return self.price


b3 = Book (title="Harry Potter", pageCount=500,
          author="J. K. Rowling", price=50)
print(b3)
print(b3.title)
print(b3.getprice())
b3.setdiscount(0.2)

b3 = Book (title="Heart", pageCount=216,
          author="Edmondo De Amicis", price=35)
print(b3)
print(b3.title)
print(b3.getprice())
b3.setdiscount(0.2)

b3 = Book (title="White Fang", pageCount=400,
          author="Jack London", price=40)
print(b3)
print(b3.title)
print(b3.getprice())
b3.setdiscount(0.2)




