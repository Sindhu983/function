# def student_burget(students,amount):
#     sum=students*amount
#     if sum<=50000:
#        print("we are in burget")
#     else:
#         print("we are out of burget")
# students=int(input("enter the students :"))
# amount=int(input('enter the amount :'))
# student_burget(students,amount)
        

num=int(input("enter te number :"))
c=num
i=0
sum=0
rem=0
count=0
while num>0:
    j=1
    while j<=num:
        #if i%j==0:
        rem=num%10
        sum=sum+rem
        num=num//10
        j+=1
    if num%sum==0:
        print(i)
    else:
        pass
    i+=1