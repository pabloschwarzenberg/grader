numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar si la llamada ocurre entre 00:00 y 07:00
if hora_llamada >= 0 and hora_llamada < 14:
    print ("Resultado: CONTESTAR")
# Verificar si la llamada ocurre antes de las 14:00, excepto si el número termina en 909
elif hora_llamada < 14 and not numero_telefonico % 100 == 909:
    print ("Resultado: NO CONTESTAR")
# Verificar si la llamada ocurre entre 17:00 y 19:00, excepto si el número comienza por 877
elif hora_llamada >= 17 and hora_llamada < 19 and not numero_telefonico // 10000000 == 877:
    print ("Resultado: NO CONTESTAR")
# En cualquier otro caso, no contestar la llamada
else:
    print ("Resultado: NO CONTESTAR")
