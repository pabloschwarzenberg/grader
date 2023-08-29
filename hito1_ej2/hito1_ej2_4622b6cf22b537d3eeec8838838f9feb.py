numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora < 14 and numero % 100 == 9:
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and numero // 1000000 == 877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
