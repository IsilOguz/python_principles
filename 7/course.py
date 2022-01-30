#Data Type =======> Dictionary (dict)
plakalar = { "İstanbul" : "34", "İzmir" : "35", "Samsun" : "55"}

print(plakalar)
print(plakalar["Samsun"])


print (plakalar)

employes = {
    "e1" : {
        "firstName" : "Ali",
        "lastName" : "Akyol",
        "jobTitle" : "Developer",
        "phoneNumber" : "537625574",
        "eMail" : "asd@hotmail.com",
    },
        "e2" : {
        "firstName" : "Ayşe",
        "lastName" : "Emin",
        "jobTitle" : "Manager",
        "phoneNumber" : "5055403244",
        "eMail" : "ayse@hotmail.com",
    },
        "e3" : {
        "firstName" : "Yağız",
        "lastName" : "Alacaoğlu",
        "jobTitle" : "Worker",
        "phoneNumber" : "5568352091",
        "eMail" : "yalaca@hotmail.com",
    }
}

# print (employes)
# print (employes["e3"])
# print (employes["e3"]["firstName"])
# print (employes["e2"]["eMail"])


code= input("Type an employe code : ")
fName= input("Type an employe name : ")
lName= input("Type an employe surname : ")
job= input("Type job title(e.g worker) : ")
phone= input("Type phone number : ")
eMail= input("Type email : ")

employes[code] = {"firstName" : "fName"}, {"lastName" , "Lname"} , { }




"""DERS NOTLARI


# Data type ===> Dictionary

# my_dict = {
#     "marka": "Renault",
#     "model": "Megane",
#     "yil" : "2015"
# }

# print(my_dict)

# plakalar = {"İstanbul": "34", "İzmir": "35", "Samsun": "55"}

# # print(plakalar)
# print(plakalar["Samsun"])

# plakalar["Ankara"] = "06"
# # print(plakalar)

# plakalar["İstanbul"] = "90"
# print(plakalar)


employees = {
    "e1": {
        "firstName": "Ali",
        "lastName": "Akyol",
        "jobTitle": "Developer",
        "phoneNumber": "6546565465",
        "eMail": "ali@hotmail.com"
    },
    "e2": {
        "firstName": "Ayşe",
        "lastName": "Ayaz",
        "jobTitle": "Manager",
        "phoneNumber": "564645652",
        "eMail": "ayse@hotmail.com"
    },
    "e3": {
        "firstName": "Mehmet",
        "lastName": "Balık",
        "jobTitle": "Worker",
        "phoneNumber": "98545664",
        "eMail": "mehmet@hotmail.com"
    },
}

# print(employees)
# print(employees["e3"])
# print(employees["e3"]["firstName"])
# print(employees["e2"]["eMail"])

code = input("Type an employee code :")
fName = input("Type an employee name :")
lName = input("Type an employee surname :")
job = input("Type job title(e.g worker) :")
phone = input("Type phone number :")
eMail = input("Type email :")

# employees[code] = {"firstName": fName, "lastName": lName,
#                    "jobTitle": job, "phoneNumber": phone, "eMail": eMail}

employees.update({
    code: {
        "firstName": fName,
        "lastName": lName,
        "jobTitle": job,
        "phoneNumber": phone,
        "eMail": eMail
    }
})

print(f"{fName} {lName} adındaki çalışanımızın telefon numarası : {phone}")
print(employees) """