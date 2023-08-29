#Contestador de celular
numero = int(input("ingrese numero telefonico: "))
hora = int(input("ingrese hora de llamada: "))
if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora >= 7 and hora < 14:
    if numero % 1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora < 19:
    if numero // 1000000 == 877:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
else:
    print("NO CONTESTAR")