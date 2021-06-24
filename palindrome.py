def palindrome(str):
    i=0
    while i<len(str):
        if str==str[::-1]:
            return "palindrome"
        else:
            return "not palindrome"
        i+=1
print(palindrome('2525'))