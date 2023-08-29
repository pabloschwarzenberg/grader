#Contestador de celular
numero=int(input("ingrese numero telefonico: "))
hora=int(input("ingrese hora de la llamada: "))
if hora>23 or hora<0:
    print("hora incorrecta")
elif numero>=100000000 or numero<1000000:
    print("numero incorrecto")
elif hora<=7:
    print("CONTESTAR")
elif hora>7 and hora<14:
    if numero%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif (hora >= 17 and hora <=19):
    if (numero>87700000):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif hora > 19:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")     