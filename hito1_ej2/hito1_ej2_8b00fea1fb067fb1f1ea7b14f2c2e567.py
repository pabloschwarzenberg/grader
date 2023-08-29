# Solicitar el número telefónico y la hora al usuario
numero_telefonico = int(input("Ingrese el número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las reglas para contestar la llamada
if hora_llamada >= 0 and hora_llamada <= 7:
    respuesta = "CONTESTAR"  # Llamada entre las 00:00 y las 07:00
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    respuesta = "CONTESTAR"  # Llamada antes de las 14:00 y número termina en 909
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico // 1000000 == 877:
    respuesta = "NO CONTESTAR"  # Llamada durante la tarde y número comienza por 877
elif hora_llamada >= 14 and hora_llamada <= 19:
    respuesta = "NO CONTESTAR"  # Llamada durante la tarde (sin excepciones)
else:
    respuesta = "NO CONTESTAR"  # Llamada después de las 19:00

# Imprimir la respuesta
print("Resultado:", respuesta)
