#Contestador de celular
a=int(input("Ingrese numero telefonico: "))
b=int(input("Ingrese hora de la llamada: "))
if 0<=b<=7:
    print("CONTESTAR")
elif b<14:
    if a%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 17<=b<=19:
    if a//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif b>19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")