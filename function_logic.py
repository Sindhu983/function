def outerFun(a, b):
    def innerFun(a,b):
        return a+b
    add = innerFun(a, b)
    return add+5
result = outerFun(5, 10)
print(result)


# def calculateSum(num):
#     if num:
#         return num + calculateSum(num-1)
#     else:
#         return 0
# res = calculateSum(10)
# print(res)


# def displayStudent(name, age):
#     print(name, age)
# displayStudent("Emma", 26)
# showStudent = displayStudent
# showStudent("Emma", 26)

def power(num):
    i=1
    new=[]
    while i<=num:
        new.append(i**2)
        i+=1
    return new
num=int(input("enter the num :"))
print(power(num))


