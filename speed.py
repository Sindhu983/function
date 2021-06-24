def driver_speed(speed):
    speed1=speed-70
    point=speed1//5
    if speed<=70:
        print("ok")
    if speed>70:
        print(point,"point")
    if point>12:
        print("lisence suspended")
speed=int(input("enter the number :"))
driver_speed(speed)
