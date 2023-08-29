# Contestar o no contestar

# Solicitar al usuario que ingrese el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar las reglas para determinar si se debe contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    # Llamada entre 00:00 y 07:00
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 1000 == 909:
    # Llamada antes de las 14:00 y número termina en 909
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and not str(numero_telefonico).startswith('877'):
    # Llamada entre 17:00 y 19:00 y número no comienza por 877
    print("Resultado: CONTESTAR")
else:
    # Resto de los casos
    print("Resultado: NO CONTESTAR")
