from typing import Counter
import requests
import json

# r = requests.get("https://restcountries.com/v3.1/name/turkey")
# result = (r.text)
# result = json.loads(result)
# print (result[0]["region"])
# print (result[0]["population"])
# print (result[0]["capital"])
# print (result[0]["borders"][1])

# r = requests.get("https://restcountries.com/v3.1/all")
# result = (r.text)
# result = json.loads(result)
# print (result[0]["capital"])
# print (result[1]["capital"])
# print (result[248]["capital"])
# counter = 0
# for i in result:
#     counter += 1
#     print(counter+0, i["name"]["official"])




# r = requests.get("https://api.frankfurter.app/latest")
# result = (r.text)
# result = json.loads(result)
# TRY = result["rates"]["TRY"]
# USD = result["rates"]["USD"]
# print (f"""1 EURO = {TRY} Turkish Liras,
#         1 EURO = {USD} Dolars
#         1 Dolar = {TRY/USD} Turkish Liras
#         """)

# r = requests.get("https://api.genelpara.com/embed/doviz.json")
# result = (r.text)
# result = json.loads(result)
# print (result["USD"]["alis"])
# print (result["EUR"]["alis"])

# for i in result.items():
#     print(i[0],i[1]["alis"])

r = requests.get("https://raw.githubusercontent.com/ozanerturk/covid19-turkey-api/master/dataset/timeline.json")

result = (r.text)
result = json.loads(result)
# print (result)

print(result["31/12/2021"]["deaths"]) 
    


