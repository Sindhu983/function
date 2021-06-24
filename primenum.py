# def prime(num):
#     i=1
#     count=0
#     while i<=num:
#         if num%i==0 :
#             count+=1
#         i+=1
#     if count==2:
#         return "prime num"
#     else:
#         return "not prime"
# num=int(input("enter the num :"))
# print(prime(num))




def prime(user): #1 to 1000 prime numbers
	i=2
	x=0
	while i>0:
		j=2
		count=0
		while j<i:
			if i%j==0:
				count=count+1
			j=j+1
		if count==0:
			print(i)
			x=x+1
		if x==user:
			break
		i+=1
user=int(input("enter the number :"))
prime(user)

