# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 8]
# for i in a:
#     if i < 5:
#         print(i)


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 8]
# b = []
# for i in a:
#     if i < 5:
#         b.append(i)
# print(b)

while True:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 8]
    print (a)

    try:
        uNum = int(input("Give me a number, I will list numbers lower than it :"))

    except:
        print("Enter only numbers please")
        continue

    for i in a:
        if i < uNum:
            print(i)

