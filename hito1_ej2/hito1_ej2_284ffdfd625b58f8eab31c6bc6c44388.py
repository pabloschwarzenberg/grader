numero = int(input("Ingrese el número de teléfono: "))
hora = int(input("Ingrese la hora actual (0-23): "))

if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora >= 7 and hora < 14 and numero % 100 == 9:
    print("CONTESTAR")
elif hora >= 17 and hora < 19 and numero // 1000000 == 877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")