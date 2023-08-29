#Contestador de celular
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora >= 7 and hora < 14 and numero % 1000 == 909:
    print("CONTESTAR")
elif hora >= 17 and hora < 19 and not str(numero).startswith("877"):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")