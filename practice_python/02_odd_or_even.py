





def my_function():

   while True:
    try:
        num = input("Enter a number (if you want quit press 'q') :")
    except:
        print("Give me only number please")
        continue

    if num == "q":
        break  
    num2=int(num)
    if num2 % 2 == 0:
        print (f"{num} is a even number.")
    else:
        print (f"{num} is a odd number")
        

my_function()
