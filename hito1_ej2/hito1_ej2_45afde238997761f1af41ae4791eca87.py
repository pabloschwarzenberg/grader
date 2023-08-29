# Solicitar al usuario el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese el número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las reglas para contestar la llamada
if hora_llamada >= 0 and hora_llamada <= 7:
    # Llamada entre 00:00 y 07:00
    print("Resultado: CONTESTAR")
elif hora_llamada < 14:
    # Llamada antes de las 14:00
    if numero_telefonico % 1000 == 909:
        # Número termina en 909
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19:
    # Llamada entre 17:00 y 19:00
    if str(numero_telefonico).startswith("877"):
        # Número comienza por 877
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
else:
    # Llamada después de las 19:00
    print("Resultado: NO CONTESTAR")


     