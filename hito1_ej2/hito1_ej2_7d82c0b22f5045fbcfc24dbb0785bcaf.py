n_telefono = int(input("Ingrese el número telefónico: "))
hora = int(input("Ingrese la hora de la llamada: "))

if hora >= 0 and hora <= 7:
    print("Contestar")
elif hora < 14:
    if n_telefono % 1000 == 909:
        print("Contestar")
    else:
        print("No contestar")
elif hora >= 17 and hora <= 19:
    if n_telefono // 1000000 == 877:
        print("Contestar")
    else:
        print("No contestar")
else:
    print("No contestar")

