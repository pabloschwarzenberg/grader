#Contestador de celular
 # Solicitar número telefónico y hora al usuario
numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar si se debe contestar la llamada
if hora_llamada >= 0 and hora_llamada <= 7:
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    print("CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and str(numero_telefonico).startswith("877"):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
