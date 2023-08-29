# Solicitar el número telefónico y la hora de la llamada al usuario
numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las reglas para determinar si contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    # Regla 1: Si la llamada ocurre entre las 00:00 y las 07:00, se contesta
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 100 == 909:
    # Regla 2: Si ocurre antes de las 14:00, se contesta si el número termina en 909
    print("CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico // 1000000 != 877:
    # Regla 3: Durante la tarde, se contesta entre las 17:00 y las 19:00, excepto si el número comienza por 877
    print("CONTESTAR")
else:
    # Regla 4: Después de las 19:00, no se contesta el celular
    print("NO CONTESTAR")