open("test.txt" )
open("test.txt" , "r")
open("test.txt" , "w")

a = open ("test.txt", "w")
a.write("Kanka")
a.close()

# RAM bilgiler siliniyor, Harddisk e yazarsak kalıcı olur

# File Handling in Python
# Opening file
# dosya açmak için open() fonksiyonu kullanılır

#open(file_name, mode)
# mode => dosyaya hangi amaçla eriştiğimizi belirtir

'''
"r" - Read(Okuma modu) - Default value. Opens a file for reading, error if the file does not exist
"a" - Append(Ekleme modu) - Opens a file for appending, creates the file if it does not exist
    dosyanın sonuna ekleme yapılır, silmez
"w" - Write(Yazma modu) - Opens a file for writing, creates the file if it does not exist
    önceden varolanlar silinir, sıfırdan yazar
"x" - Create(Oluşturma) - Creates the specified file, returns an error if the file exists


In addition you can specify if the file should be handled(işleme) as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''
# open("test.txt")

# open("test.txt", "r")
# open("test.txt", "w")
# open("test2.txt", "w")

# f = open("test.txt")
# print(f)
# f = open("test.txt", "r")
# print(f)
# f.close()

# f = open("test.txt", "w")
# print(f)
# f.close()                         #kodu siler


# f = open("test.txt", "w")
# f.write("Selam")
# f.close()

# f = open("test.txt", "w")
# print(f)
# f.write("I love python, Işıl")
# f.close()        #Türkçe karakter hatası


f = open("test.txt", "w", encoding="utf-8")
print(f)
f.write("I love python, Işıl")
f.close()  






