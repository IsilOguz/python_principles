#myList = ["Erzincan", "Ankara", "Malatya"]
# for i in myList:
#     print (i)



# myDict = {"name":"Burhan", "surname":"Altıntop", "phone":{"home":"12345", "work":"54321", },
#          "favCities":["Erzincan", "Ankara", "Malatya"]}
#for i in myDict.items():
#     # print (f"{key}-{value}")
#     if type(i[1]) == dict:
#         print(i[1]["work"])
#         print(i[1]["home"])
# artist =[
#     {"name":"Burhan", "surname":"Altıntop", "phone":{"home":"12345", "work":"54321", },"favCities":["Erzincan", "Ankara", "Malatya"]},
#     {"name":"Kemal", "surname":"Sunal", "phone":{"home":"12345", "work":"54321", },"favCities":["Erzincan", "Ankara", "Malatya"]},
#     {"name":"Adile", "surname":"Naşit", "phone":{"home":"12345", "work":"54321", },"favCities":["Erzincan", "Ankara", "Malatya"]}
#     ]   

# for i in artist:
#     print (i["name"])
#     for city in i["favCities"]:
#         print (city)

import requests
import json

r = requests.get("https://restcountries.com/v3.1/name/turkey")
r2 = r.text
r3 = json.loads(r2)

print (r3[0]["region"])
print (r3[0]["flags"]["png"])
print (r3[0]["borders"][-2])
print (r3[0]["independent"])