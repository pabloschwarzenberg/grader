telefono = int(input("Ingrese el número de teléfono (8 dígitos): "))

hora = int(input("Ingrese la hora de la llamada (0-23): "))

if hora >= 0 and hora <= 7:
    print("Resultado: CONTESTAR")
elif hora < 14 and (telefono - 909) % 2 == 0  :
    print("Resultado: CONTESTAR")
elif hora >= 17 and hora <= 19 and str(telefono).startswith("877"):
    print("Resultado: NO CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")