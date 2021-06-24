def drinks(kid,teen,young,adult):
    if kid<14:
        print("toddy")
    if teen<18:
        print("cock")
    if young<21:
        print("beer")
    if adult>21:
        print("wisky")
    else:
        print("wrong input")
kid=int(input("enter the input :"))
teen=int(input("enter the input :"))
young=int(input("enter the input :"))
adult=int(input("enter the input :"))
drinks(kid,teen,young,adult)