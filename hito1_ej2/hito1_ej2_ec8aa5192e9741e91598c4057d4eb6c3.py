numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

if hora_llamada >= 0 and hora_llamada <= 7:
    resultado = "CONTESTAR"
elif hora_llamada < 14 and str(numero_telefonico)[-3:] == "909":
    resultado = "CONTESTAR"
elif hora_llamada >= 17 and hora_llamada <= 19 and str(numero_telefonico)[:3] != "877":
    resultado = "CONTESTAR"
else:
    resultado = "NO CONTESTAR"

print("Resultado:", resultado)
