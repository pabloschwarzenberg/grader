#Contestador de celular
numero_telefonico = str(input("Ingrese el número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))


contestar = False

if hora_llamada >= 0 and hora_llamada <= 7:
    contestar = True
elif hora_llamada < 14 and numero_telefonico.endswith("909"):
    contestar = True
elif hora_llamada >= 17 and hora_llamada <= 19 and not numero_telefonico.startswith("877"):
    contestar = True


if contestar:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")