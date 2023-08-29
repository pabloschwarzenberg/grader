#Contestador de celular
numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

if hora_llamada >= 0 and hora_llamada <= 7:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and numero_telefonico[-3:] == "909":
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and not numero_telefonico.startswith("877"):
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
