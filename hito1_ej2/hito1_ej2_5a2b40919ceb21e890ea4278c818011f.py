#Contestador de celular
numero = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de la llamada: "))

if hora >= 0 and hora <=7:
    print("CONTESTAR")
elif hora >= 8 and hora <= 14:
    if numero % 1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora <= 19:
    if numero // 100000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")