numero = int(input("Ingrese número telefónico (8 dígitos): "))
hora = int(input("Ingresa  hora de la llamada (0-23): "))

if hora >= 0 and hora < 7:
    print("CONTESTAR")
elif hora < 14:
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

      