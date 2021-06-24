def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(num1,"num1 is greater")
    elif num2>num3 and num2>num1:
        print(num2,"num2 is greater")
    else:
        print(num3,"num3 is greater")
num1=int(input("enter the 1st num :"))
num2=int(input('entrer the 2nd num :'))
num3=int(input("enter the 3rd num :"))
maximum(num1,num2,num3)