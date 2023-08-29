telefono = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada (0-23): "))
contestar = False
if hora >= 0 and hora <= 7:
    contestar = True
elif hora < 14 and telefono % 100 == 9:
    contestar = True
elif hora >= 17 and hora <= 19 and telefono // 10000000 == 877:
    contestar = True
if contestar:
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")