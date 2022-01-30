import json

def addContacts():
    id = int(input("Contact Id : "))
    name = input("Contact Name : ")
    surname = input("Contact Surname : ")
    phone = input("Contact Phone : ")
    address = input("Contact Adress : ")
    contact = {"id": id, "name": name, "surname": surname,
               "phone": phone, "address": address}
    # print(contact)
    with open("contacts.txt", "r+", encoding="utf-8") as f:
        textList = f.readlines()
        print(textList)
        textList.insert(-1, str(contact) + ",\n")
        f.seek(0)
        f.writelines(textList)


def listContacts():
    with open("contacts.txt", "r", encoding="utf-8") as f:
        textlist = f.readlines()
        # print(textlist)
        textlist = textlist[1:-1]
        # print(textlist)
        for i in textlist:
            # print(i)
            cleantext = i[:-2]
            # print(cleantext)
            cleantext = cleantext.replace("\'", "\"")
            # print(type(cleantext))
            jsonline = json.loads(cleantext)
            # print(jsonline)
            # print(jsonline["name"])
            print(jsonline["id"], "-", jsonline["name"],
                  jsonline["surname"], jsonline["phone"], jsonline["address"])


while True:
    choice = int(input("""
            1- Add Contact
            2- List Contact

            Type your choice :"""))
    if choice == 1:
        addContacts()
    elif choice == 2:
        listContacts()


    
