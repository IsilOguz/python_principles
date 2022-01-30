import random


def addCostumer():
    name = input("New Customer Name :")
    name.capitalize()
    surname = input("New Customer Surname :")
    surname.capitalize
    phone = input("New Customer Phone :")
    balance = int(input("Customer Balance :"))
    num = random.randint(10000, 99999)
    newCustomer = {"costumerNum": num,  "name": name, "surname": surname, "phone": phone, "balance": balance}
    #print (newCustomer)
    with open("customers.txt", "r+", encoding="utf-8") as f:
        customerList = f.readlines()
        #print(customerList)
        customerList.insert(0, str(newCustomer) + "\n")
        #print(customerList)
        f.seek(0)
        f.writelines(customerList)
    print (f"Acount created successfully! Your account number is :{num}")

def withdraw():
    print("Withdraw function will written")
    pass

def learnBalance():
    print("LearnBalance function will written")
    pass

while True:
    try:
        choice = int(input("""
                1-)Add Customer
                2-)Withdraw
                3-)Learn Balance
                4-)Exit
                
                Choose an option :"""))
    
    except:
        print("Please choose right option")
        continue
 
    if choice == 1:
        addCostumer()

    elif choice == 2:
        withdraw()

    elif choice == 3:
        learnBalance()



    elif choice == 4:
        print ("Good Bye...")
        break

    else:
        print("Please choose right option")