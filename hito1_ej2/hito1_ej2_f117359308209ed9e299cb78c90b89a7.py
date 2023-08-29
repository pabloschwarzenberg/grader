# Obtener el número telefónico y la hora de la llamada desde el usuario
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar las reglas para determinar si contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    # Regla 1: Si la llamada ocurre entre 00:00 y 07:00, contestar
    print("Resultado: CONTESTAR")
elif hora_llamada < 14:
    # Regla 2: Si ocurre antes de las 14:00, no contestar, excepto si el número termina en 909
    if numero_telefonico % 1000 == 909:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19:
    # Regla 3: Durante la tarde, contestar entre 17:00 y 19:00, excepto si el número comienza por 877
    if str(numero_telefonico)[0:3] == "877":
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
else:
    # Regla 4: Después de las 19:00, no contestar el celular
    print("Resultado: NO CONTESTAR")
