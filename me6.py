# def names(list):
#     i=0
#     new=[]
#     while i<len(list):
#         if list[i] not in new:
#             new.append(list[i])
#         i+=1
#     print(new)
# list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# names(list)


# def names(list1):
#     a=list(set(list1))
#     print(a)
# list1 = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
# names(list1)

 
def duplicate(names):
    i=0
    count=0
    while i<len(names):
        if names.count(names[i])>1:
            names.remove(names[i])
        i+=1
    return names
names = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
print(duplicate(names))


# def names(list1):
#     i=0
#     list2=0
#     while i<len(list1):
#         list2 = list(dict.fromkeys(list1))
#         i+=1
#     return list2  
# list1 = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
# print(names(list1))



