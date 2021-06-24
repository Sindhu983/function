def factorial(num):
    i=1
    fact=1
    while i<=num:
        fact=fact*i
        i+=1
    return fact
num=int(input("enter the number :"))
print(factorial(num))