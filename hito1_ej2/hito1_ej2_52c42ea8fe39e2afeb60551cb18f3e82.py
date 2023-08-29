# Preguntar al usuario por la hora y el número de celular
numero = int(input("Ingrese el número de celular (8 dígitos): "))
hora = int(input("Ingrese la hora (0-23): "))


# Verificar las reglas para contestar la llamada
if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora < 14:
    if str(numero)[-3:] == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora < 19:
    if not str(numero).startswith("877"):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
     