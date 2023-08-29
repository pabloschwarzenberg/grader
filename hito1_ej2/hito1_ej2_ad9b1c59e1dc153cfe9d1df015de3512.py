a=int(input("ingrese un numero telefonico: "))
b=int(input("ingrese hora de llamada: "))
if 0<=b<=7:
    print("CONTESTAR")
elif b>19:
    print("NO CONTESTAR")
elif 7<b<14:
    if a%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17<=b<=19:
    if a//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
