#Contestador de celular
 # Obtener el número telefónico y la hora de la llamada del usuario
numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las reglas para decidir si contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    # Llamada entre 00:00 y 07:00
    print("Resultado: CONTESTAR")
elif hora_llamada < 14:
    # Llamada antes de las 14:00
    if numero_telefonico % 100 == 9:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19:
    # Llamada entre 17:00 y 19:00
    if numero_telefonico // 10000000 == 877:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
else:
    # Llamada después de las 19:00
    print("Resultado: NO CONTESTAR")     