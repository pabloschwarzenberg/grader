numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada: "))

if hora_llamada >= 0 and hora_llamada <= 7:
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico.endswith("909"):
    print("CONTESTAR")
elif (hora_llamada >= 17 and hora_llamada <= 19) and not numero_telefonico.startswith("877"):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")