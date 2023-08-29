#Contestador de celular
numero=int(input("Ingrese el número de calular: "))
hora=int(input("Ingrese la hora, solo números enteros: "))

if(0<=hora<=7):
    print("CONTESTAR")
elif(7<hora<14):
    if(numero%1000==909):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif(17<=hora<=19):
    if(87700000<=numero<87800000):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
