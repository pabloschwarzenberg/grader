numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada (formato 24 horas): "))

contestar = False

if hora_llamada >= 0 and hora_llamada < 7:
    contestar = True
elif hora_llamada < 14 and numero_telefonico[-3:] == "909":
    contestar = True
elif hora_llamada >= 17 and hora_llamada < 19 and not numero_telefonico.startswith("877"):
    contestar = True

if contestar:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")