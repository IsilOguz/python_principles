

# üstteki formata göre kullanıcadan 3 ürün bilgisi alarak,

# 1-) print(f"") metoduyla 3 ürünün bilgileri aşağıdaki şekilde ekrana yazdırın.
# "{Elektronik} reyonunda satılan {Samsung Galaxy S10} isimli ürünün fiyatı {8000} TL dir. Stokta {500} adet bulunmaktadır"

# 2-) products dictionary ye kullanıcıdan aldığınız 3 üründe ekleyin
#  oluşan dictionary i ekrana yazdırın.


urunAdi = input ("Type a product name : ")
urunReyon = input ("Type this product's type : ")
urunFiyati = input ("Type this product's price : ")
urunSayisi = input ("Type this product's quantity : ")
print (f"{urunReyon} reyonunda satılan {urunAdi} isimli ürünün fiyatı {urunFiyati} TL dir. Stokta {urunSayisi} adet bulunmaktadır. ")

urunAdi2 = input ("Type a product name : ")
urunReyon2 = input ("Type this product's type : ")
urunFiyati2 = input ("Type this product's price : ")
urunSayisi2 = input ("Type this product's quantity : ")
print (f"{urunReyon2} reyonunda satılan {urunAdi2} isimli ürünün fiyatı {urunFiyati2} TL dir. Stokta {urunSayisi2} adet bulunmaktadır. ")

urunAdi3 = input ("Type a product name : ")
urunReyon3 = input ("Type this product's type : ")
urunFiyati3 = input ("Type this product's price : ")
urunSayisi3 = input ("Type this product's quantity : ")
print (f"{urunReyon3} reyonunda satılan {urunAdi3} isimli ürünün fiyatı {urunFiyati3} TL dir. Stokta {urunSayisi3} adet bulunmaktadır. ")




products = {
    "product01": {
        "name": "Samsung Galaxy S10",
        "type": "Elektronik",
        "pQuantity": 500,
        "price": 8000
    },
        "product02": {
        "name": urunAdi,
        "type": urunReyon,
        "pQuantity": urunSayisi,
        "price": urunFiyati
    },
        "product03": {
        "name": urunAdi2,
        "type": urunReyon2,
        "pQuantity": urunSayisi2,
        "price": urunFiyati2
    },        
        "product04": {
        "name": urunAdi3,
        "type": urunReyon3,
        "pQuantity": urunSayisi3,
        "price": urunFiyati3
    },
}

print (products)

