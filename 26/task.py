
"""
https://jsonplaceholder.typicode.com/todos
yapısını inceleyelim

request ve json modüllerini kullanarak

1- userId 1 in tüm görevlerini yazdırınız


2- userId 2 için tamamlanmış görevleri yazdırın

3- userId 10 için tamamlanmış görevleri yazdırn
"""
import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")
r2 = r.text
r3 = json.loads(r2)

for i in r3:
    if i["userId"] == 1:
        print (i["title"])

    # if i["userId"] == 2 and i["completed"] == False:
    #     print (i["title"])
    
    # if i["userId"] == 10 and i["completed"]:
    #     print (i["title"])

