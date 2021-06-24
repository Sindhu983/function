def square():
    i=0
    rem=0
    user=int(input("enter the number :"))
    while user>0:
        rem=user%10
        user=user//10
        result=rem*rem
        print(result,end='') 
square()
