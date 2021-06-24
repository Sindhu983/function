def harshad(num):
    d=num
    i=0
    sum=0
    while num>0:
        rem = num%10
        sum=sum+num
        num=num//10
    if num%sum==0:
        print("harshad num")
    else:
        print("not harshad num")
num=int(input("enter the num :"))
harshad(num)

    
