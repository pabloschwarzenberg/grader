#Contestador de celular
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

if hora_llamada >= 0 and hora_llamada < 7:
    print("CONTESTAR")
elif hora_llamada < 14 and not str(numero_telefonico)[-3:] == "909":
    print("NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and not str(numero_telefonico).startswith("877"):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
      