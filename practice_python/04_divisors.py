while True:
    
    try:
        num = int(input("Enter a number :"))
    except:
        print("Enter only numbers please.")

    print (f"{num}'s divisors are: ")
    for number in range(2,num):
        if (num % number) == 0:
            print (number)