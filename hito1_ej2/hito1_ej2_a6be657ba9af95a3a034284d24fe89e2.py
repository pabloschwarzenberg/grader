numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

if (0 <= hora < 7) or (7 <= hora < 14 and str(numero).endswith("909")) or (17 <= hora < 19 and not str(numero).startswith("877")):
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
