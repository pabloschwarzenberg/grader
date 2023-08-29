#Contestador de celular
telefono=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de llamada: "))
b=telefono%1000
c=telefono//100000

if hora>=0 and hora<=7:
    print("CONTESTAR")
elif hora>7 and hora<14:
    if b==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora>=17 and hora<=19:
    if  c==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora>19:
    print("NO CONTESTAR")