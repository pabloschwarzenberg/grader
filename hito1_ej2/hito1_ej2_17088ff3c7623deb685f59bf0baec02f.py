numero_telefonico = input("Ingrese número telefónico (8 cifras): ")
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

contestar = False

if hora_llamada >= 0 and hora_llamada <= 7:
    contestar = True
elif hora_llamada < 14 and numero_telefonico[-3:] == '909':
    contestar = True
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico[:3] != '877':
    contestar = True

if contestar:
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")