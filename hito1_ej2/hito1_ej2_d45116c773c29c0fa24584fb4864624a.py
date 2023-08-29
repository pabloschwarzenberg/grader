numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

if hora_llamada >= 0 and hora_llamada <= 7:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 1000 == 909:
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and str(numero_telefonico).startswith('877'):
    print("Resultado: NO CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
