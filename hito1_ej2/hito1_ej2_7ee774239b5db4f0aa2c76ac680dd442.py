#Contestador de celular
numero = int(input("Ingrese número telefónico (8 dígitos): "))
hora = int(input("Ingrese hora de la llamada (0-23): "))

if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora >= 7 and hora < 14:
    if numero % 100 == 9:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora < 19:
    if numero // 1000000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
