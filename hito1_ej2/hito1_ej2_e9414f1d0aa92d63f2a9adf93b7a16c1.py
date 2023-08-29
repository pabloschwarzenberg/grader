# Solicitar al usuario el número telefónico y la hora de la llamada
numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar las reglas para decidir si contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico[-3:] == "909":
    print("CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico.startswith("877"):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
