a=input("ingresar número de teléfono: ")
b=int(input("hora de llamada: "))
if 0<=b<=7:
    print ("CONTESTAR")
elif b<14:
    if a[5:8]=="909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17<=b<=19:
    if a[0:3]=="877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif b>19:
    print("NO CONTESTAR")
