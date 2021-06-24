def same_num(list1,list2):
    i=0
    new=[]
    while i<len(list1):
        if list1[i] in list2:
            new.append(list1[i])
            new.sort()
        i+=1
    return new
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
print(same_num(list1,list2))