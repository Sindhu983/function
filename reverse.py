def string_reverse(str):
    rstr=''
    i=0
    lenstr=len(str)
    while lenstr>0:
        rstr=rstr+str[lenstr-1]
        lenstr-=1
    return rstr
print(string_reverse('123pqrs'))

# def reverse(str):
#     i=-1
#     while i>=-len(str):
#         print(str[i])
#         i-=1
# str='123mno'
# reverse(str)
    


