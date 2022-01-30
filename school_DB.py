from tabulate import tabulate

students = [
    {"sNumber": 101,
     "name": "Ali",
     "surname": "Ak", 
     "phone": "12345" ,
     "wallet": 1000},
    
    {"sNumber": 102,
     "name": "Ayşe",
     "surname": "Al",
     "phone": "99999" ,
     "wallet": 500},
    
    {"sNumber": 103,
     "name": "Zeynep",
     "surname": "Yıldırım", 
     "phone": "21222" , 
     "wallet": 900},
    
    {"sNumber": 104,
     "name": "Mehmet",
      "surname": "Gök", 
      "phone": "13579" ,
       "wallet": 400}
]


def saveStu(sNumber,sName,sSurname,sPhone,wallet):
    sNumberList = []
    for i in students:
        sNumberList.append(i["sNumber"])
        if sNumber in sNumberList:
            sNumber= int(input("Wrong student number :/ Please try again :"))
            print (f"Last student number is : {sNumberList[-1]}")
            break
    students.append({"sNumber":sNumber, "name":sName, "surname":sSurname, "phone":sPhone , "wallet":wallet })
    

def listStu():
    print (tabulate(students, headers="keys"))

def addMoneyToWallet(sNumber, amount):

    for i in students:
        if i["sNumber"] == sNumber:
            i["wallet"] +=amount

def shoppingFromCanteen(sNumber,info,amount):
    for student in students:
        if student in students:
            if student["sNumber"]== sNumber:
                student['wallet'] -= amount
                print(f"{amount} TL for {info}.")
                print(f"Student Number {sNumber}, new wallet balance: {student['wallet']}")
    
def updateStu(sNumber):
        for stu in students:
            if stu["sNumber"] == sNumber:
                print (stu)
                print (f"For the student number : {stu['sNumber']}")
                sName = input("New Student Name :")
                sSurname = input("New Student Surname :")
                sPhone = input("New Student Phone Number :")
                wallet = input("New Wallet Balance :")
                stu["name"] = sName
                stu["surname"] = sSurname
                stu ["phone"] = sPhone
                stu["wallet"] = wallet
                print (f"Student number {sNumber} is updated")

def menu():
    while True:

        choice = input("""Type your choice :
        1 - List all students 
        2 - Add new student
        3 - Add balance to a student
        4 - Shopping from canteen 
        5 - Edit a student

        To quit, type 'q'
        please choose an option from menu :""")

        print ("\n".center(2, " "))

        if choice == "q":
            break
        elif choice == "1":
            listStu()
        elif choice == "2":
            sNumber = int(input("Student Number :"))
            sName = input("Student Name :")
            sSurname = input("Student Surname :")
            sPhone = input("Student Phone Number :")
            wallet = input("Wallet Balance :")
            saveStu(sNumber,sName,sSurname,sPhone,wallet)
            
        elif choice == "3":
            sNumber = int(input("Student Number :"))
            amount = int (input("Balance to add :"))
            addMoneyToWallet(sNumber, amount)

        elif choice == "4":
            sNumber = int(input("Student number :"))
            info = input("Information :")
            amount = int(input("Balance to deduct :"))
            shoppingFromCanteen(sNumber,info,amount)

        elif choice == "5":
            sNumber = int(input("Student Number To Update:"))
            updateStu(sNumber)

        else:
            continue

        print ("\n ".center(101, " "))
        

                    
        
        
print("\n")
print("*".center(50, "-"))
print("Welcome to our School Database".center(50, "-"))
menu()




