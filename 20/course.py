# open(file_name, mode)

# f = open("file.txt")
# print (f)
# f.close()

# f = open("file.txt", "w")
# f.write("selam")
# f.close()

# f = open("file.txt", "a", encoding="utf-8")
# f.write("Merhaba dünya sıkıldım senden")
# f.close()

# f = open("file.txt", "a", encoding="utf-8")
# f.write("\n Merhaba dünya sıkıldım senden")
# f.close()

# try:
#     f = open("file2.txt", "x", encoding="utf-8")
#     f.write("Birşeyler yazıyorum")
#     f.close()

# except FileExistsError:
#     print("dosya bulunamadı")

# finally:
#     print ("işlem tamamlandı")

# f = open("file.txt", "r", encoding="utf-8")
# text = f.read()
# print (text)

# f.close()
# f = open("file.txt", "r", encoding="utf-8")
# text = f.readline()
# print (text, end="")
# text2= f.readline()
# print (text2, end="")
# text3= f.readline()
# print (text3, end="")
# text4= f.readline()
# print (text4, end="")

# f = open("file.txt", "r", encoding="utf-8")
# textList= f.readlines()
# print(textList[1])
# f.close()

with open("file.txt", "r", encoding="utf-8") as f:
    text= f.read(40)
    print(f.tell())
    print(text)
    f.close()