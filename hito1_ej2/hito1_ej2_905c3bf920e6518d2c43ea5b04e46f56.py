# Obtener el número telefónico y la hora de la llamada del usuario
numero_telefonico = input("Ingrese número telefónico (8 dígitos): ")
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar las reglas para contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    # Si la llamada ocurre entre 00:00 y 07:00, se contesta
    print("Resultado: CONTESTAR")
elif hora_llamada < 14:
    # Si ocurre antes de las 14:00, no se contesta, excepto si el número termina en 909
    if numero_telefonico[-3:] == "909":
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19:
    # Durante la tarde (17:00-19:00), se contesta exceptuando un número que comienza por 877
    if numero_telefonico[:3] == "877":
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
else:
    # Después de las 19:00, no se contesta
    print("Resultado: NO CONTESTAR")