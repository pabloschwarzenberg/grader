numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

# Reglas para contestar automáticamente
if hora_llamada >= 0 and hora_llamada <= 7:
    print("CONTESTAR")
elif hora_llamada < 14:
    if str(numero_telefonico)[-3:] == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19:
    if str(numero_telefonico)[:3] == "877":
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")
