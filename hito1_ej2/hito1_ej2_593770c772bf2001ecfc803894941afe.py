#Contestador de celular
numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))
contestar_llamada = False
if hora_llamada >= 0 and hora_llamada < 7:
    contestar_llamada = True
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    contestar_llamada = True
elif hora_llamada >= 17 and hora_llamada < 19 and numero_telefonico // 1000000 == 877:
    contestar_llamada = True
if contestar_llamada:
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")       