numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

if hora_llamada >= 0 and hora_llamada < 7:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and not str(numero_telefonico)[-3:] == "909":
    print("Resultado: NO CONTESTAR")
elif hora_llamada >= 13 and hora_llamada < 19 and not str(numero_telefonico)[:3] == "877":
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")