# Solicitar al usuario el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar las reglas para determinar si se contesta o no la llamada
if hora_llamada >= 0 and hora_llamada <= 7:
    # Llamada entre 00:00 y 07:00
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and str(numero_telefonico)[-2:] == '09':  # Verificar si el número termina en 09
    # Llamada antes de las 14:00 y número termina en 09
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada < 19 and str(numero_telefonico).startswith('877'):
    # Llamada entre 17:00 y 18:59 y número empieza por 877
    print("Resultado: CONTESTAR")
else:
    # En cualquier otro caso, no contestar la llamada
    print("Resultado: NO CONTESTAR")