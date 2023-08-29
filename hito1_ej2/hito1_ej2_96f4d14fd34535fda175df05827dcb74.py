#Contestador de celular
# Solicitar el número telefónico y la hora de la llamada al usuario
numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las reglas para determinar si se contesta o no
if hora_llamada >= 0 and hora_llamada < 7:
    # Llamada entre 00:00 y 07:00, se contesta
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 1000 == 909:
    # Llamada antes de las 14:00 y número termina en 909, se contesta
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada < 19 and str(numero_telefonico).startswith("877"):
    # Llamada entre 17:00 y 19:00 y número comienza por 877, se contesta
    print("Resultado: NO CONTESTAR")
else:
    # En cualquier otro caso, no se contesta
    print("Resultado: NO CONTESTAR")




      