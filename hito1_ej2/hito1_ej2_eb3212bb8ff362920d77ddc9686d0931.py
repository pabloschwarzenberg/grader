#Contestador de celular
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

if hora_llamada >= 0 and hora_llamada <= 7:
    print("CONTESTAR")
elif hora_llamada < 14:
    if numero_telefonico % 100 == 9:
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