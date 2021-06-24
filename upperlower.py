def upper(str):
    d={'upper_case':0,'lower_case ':0}
    i=0
    count=0
    count1=0
    while i<len(str):
        if str[i].isupper():
            count+=1
        elif str[i].islower():
            count1+=1
        else:
            pass
        i+=1
    print("Upper case letters :",count)
    print("Lower case letters :",count1)
upper("The quick Brown Fox")