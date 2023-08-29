numero_telefono = int(input("Ingresa el número de teléfono (8 cifras): "))
hora_llamada = int(input("Ingresa la hora de la llamada (0-23): "))

if hora_llamada >= 0 and hora_llamada <= 7:
    print("Contestar llamada: Sí")
elif hora_llamada < 14 and numero_telefono % 1000 == 909:
    print("Contestar llamada: Sí")
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefono // 100000 == 877:
    print("no contestar")
else:
    print("no contestar")
