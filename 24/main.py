from os import name
import random
import json

def addCostumer():
    name = input("New Customer Name :").capitalize()
    surname = input("New Customer Surname :").capitalize()
    phone = input("New Customer Phone :")
    balance = int(input("Customer Balance :"))
    num = random.randint(10000, 99999)
    newCustomer = {"customerNum": num,  "name": name, "surname": surname, "phone": phone, "balance": balance}
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
    with open("customers.txt", "r", encoding="utf-8") as f:
        customerList = []
        textList = f.readlines()
        #print(textList)
        for i in textList:
            #print (i)
            i = i.replace("\'", "\"")
            jsonCustomer =json.loads(i)
            # print (jsonCustomer["name"])
            customerList.append(jsonCustomer)
        #print (customerList)
        print ("To withdraw from your account, please enter your information.")
        name = input("Enter customer name :").capitalize()
        customerNum = int(input("Enter customer number :"))
        for i in customerList:
            if name == i["name"] and customerNum == i["customerNum"]:
                balance = int(input("How much do you want to withdraw :"))
                i["balance"] -= balance
                print (f"Customer Number : {customerNum} , New Balance : {i['balance']}")

        with open("customers.txt", "w", encoding="utf-8") as f:
            counter = 0
            for i in customerList:
                counter +=1
                if counter == len(customerList):
                    f.write(str(i))
                else:
                    f.write(str(i)+"\n")

def learnBalance():
        with open("customers.txt", "r", encoding="utf-8") as f:
            customerList = []
            textList = f.readlines()
            for i in textList:
                i = i.replace("\'", "\"")
                jsonCustomer =json.loads(i)
                # print (jsonCustomer)
                # print (type (jsonCustomer["customerNum"]))
                customerList.append(jsonCustomer)
            print ("To learn balance, please enter your information :")
            name = input("Customer name :")
            customerNum = int(input("Customer number :"))
            for i in customerList:
                if name == i["name"] and customerNum == i["customerNum"]:
                    print(f"Customer Number : {i['customerNum']}, Your Balance : {i['balance']}")

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