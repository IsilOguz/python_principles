"""
kullanıcıdan bir küçük sayı, bir de büyük sayı isteyin
bu iki sayı arasındaki asal sayıları yazdırın
"""

smallNum = int(input("Enter a number :"))
bigNum = int(input("Enter a number again :"))

print (f"Prime numbers between {smallNum} and {bigNum} :")
for num in range(smallNum,bigNum + 1):
    # print(num)
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0: 
                break
        else:
            print(num)

 

