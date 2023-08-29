numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

if 0 <= hora <= 7:
    print("CONTESTAR")
elif hora < 14 and numero % 100 == 909:
    print("CONTESTAR")
elif hora < 14:
    print("NO CONTESTAR")
elif 17 <= hora <= 19 and str(numero).startswith("877"):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
