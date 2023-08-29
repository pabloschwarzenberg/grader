R=int(input("por favor ingrese su rut"))

cal= (R//10000000)*3
cal2= ((R//1000000)%10)*2
cal3= ((R//100000)%10)*7
cal4= ((R//10000)%10)*6
cal5= ((R//1000)%10)*5
cal6= ((R//100)%10)*4
cal7= ((R//10)%10)*3
cal8= ((R//1)%10)*2

S= cal + cal2 + cal3 + cal4 + cal5 + cal6 + cal7 + cal8

rest = S//11

rest2 = S -(11* rest)

rest3 = 11 - rest2

if rest3 == 11:
    print("DV=", end="")
    print(0)
elif rest3 == 10:
    print("DV=", end="")
    print("k")
else:
    print("DV=", end="")
    print(rest3)
