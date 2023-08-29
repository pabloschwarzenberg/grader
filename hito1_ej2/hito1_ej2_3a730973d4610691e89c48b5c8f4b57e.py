a=int(input("Ingrese un numero telefonico"))
b=int(input("Ingrese hora de llamada"))

if 0<=b<=7:
    print("CONTESTAR")

if b<14 and 11111909<=a<=99999909:
    print("CONTESTAR")

else:
    print("NO CONTESTAR")

if 17<=b<=19:
    print("CONTESTAR")

if 17<=b<=19 and 87700000<=a<=87799999:
    print("NO CONTESTAR")

if b>19:
    print("NO CONTESTAR")
