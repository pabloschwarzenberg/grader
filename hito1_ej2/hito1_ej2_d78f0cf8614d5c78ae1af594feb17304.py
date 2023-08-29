numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

contestar = False

if hora_llamada >= 0 and hora_llamada <= 7:
    contestar = True
elif hora_llamada < 14:
    if numero_telefonico % 1000 == 909:
        contestar = True
elif hora_llamada >= 17 and hora_llamada <= 19:
    if str(numero_telefonico)[-3:] == "877":
        contestar = True

if contestar:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")