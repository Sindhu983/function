def one_time(list1,list2):
    list1.extend(list2)
    i=0
    new=[]
    while i<len(list1):
        if list1[i] not in new:
            new.append(list1[i])
        i+=1
    return new
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
print(one_time(list1,list2))
