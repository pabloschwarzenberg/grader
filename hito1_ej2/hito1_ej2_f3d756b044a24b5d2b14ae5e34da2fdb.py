#Contestador de celular
numero_telefonico = int(input("Ingrese número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

if hora_llamada >= 0 and hora_llamada < 14:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14:
    if numero_telefonico % 100 == 909:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada < 19:
    if str(numero_telefonico)[0:3] == "877":
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")