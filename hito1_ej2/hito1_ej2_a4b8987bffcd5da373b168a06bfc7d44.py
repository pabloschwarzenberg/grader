#Contestador de celular
hora = int(input("Ingresa la hora del día (0-23): "))
numero = int(input("Ingresa el número de teléfono (8 dígitos): "))

if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora < 14:
    if numero % 1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora < 19:
    if numero // 100000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
      