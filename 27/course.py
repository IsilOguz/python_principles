myCities = [
    {"title" : "Erzincan", "trafficCode" : "24", "destinations" : ["Terzi Baba Türbesi", "Girlevik Şelalesi", "Otlukbeli Gölü"], "foods" : {"tulum peyniri" : "Akpınar Tulum Peyniri", "Cimin üzümü" : "Erzincan Restoran", "simit" : "Simit Sarayı"}},
    {"title" : "Malatya", "trafficCode" : "44", "destinations" : ["Su Sesi", "Battalgazi Ulu Camii", "Hayvanat Bahçesi"], "foods" : {"kayısı" : "Mini Hal", "gırık" : "Köfteci Ali Usta", "kayısılı kavurma" : "Kayısı Restoran"}},
    {"title" : "Ankara", "trafficCode" : "06", "destinations" : ["Ankara Kalesi", "Kocatepe Camii", "Ahter"], "foods" : {"Beypazarı Kurusu" : "Beypazarı Restoran", "Tamdak Tiridi" : "Mehmet Usta", "ankara simiti" : "Simit Sarayı"}},
]

# for i in myCities:
#     print ("\n",i["title"])
#     for destination in i["destinations"]:
#         print(destination)

for i in myCities:
    print ()
    print (i["title"])
    for food,place in i["foods"].items():
        print(food, "-", place)