numero_telefonico = input("Ingrese el número telefónico (8 dígitos): ")
hora_llamada = int(input("Ingrese la hora de la llamada (formato 24 horas): "))

if hora_llamada >= 0 and hora_llamada < 7:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and numero_telefonico[-3:] == '909':
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada < 19 and not numero_telefonico.startswith("877"):
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")