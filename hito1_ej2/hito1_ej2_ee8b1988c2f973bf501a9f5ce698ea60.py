# Solicitar el número telefónico y la hora de la llamada al usuario
numero_telefonico = int(input("Ingrese el número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las condiciones para contestar o no la llamada
if hora_llamada >= 0 and hora_llamada <= 7:
    # Se contesta si la llamada ocurre entre las 00:00 y las 07:00
    respuesta = "CONTESTAR"
elif hora_llamada < 14 and numero_telefonico % 1000 == 909:
    # Se contesta si la llamada ocurre antes de las 14:00 y el número termina en 909
    respuesta = "CONTESTAR"
elif hora_llamada >= 17 and hora_llamada <= 19 and not str(numero_telefonico).startswith('877'):
    # No se contesta si la llamada ocurre entre las 17:00 y las 19:00 y el número no comienza por 877
    respuesta = "NO CONTESTAR"
else:
    # No se contesta en los demás casos
    respuesta = "NO CONTESTAR"

# Imprimir el resultado
print("Resultado:", respuesta)
