#Contestador de celular
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

# Verificar si la llamada ocurre entre las 00:00 y las 07:00
if hora_llamada >= 0 and hora_llamada <= 7:
    print("CONTESTAR")

# Verificar si la llamada ocurre antes de las 14:00, excepto si el número termina en 909
elif hora_llamada < 14 and not numero_telefonico % 100 == 909:
    print("NO CONTESTAR")

# Verificar si la llamada ocurre entre las 17:00 y las 19:00, excepto si el número comienza por 877
elif hora_llamada >= 17 and hora_llamada < 19 and not numero_telefonico // 10000000 == 877:
    print("CONTESTAR")

# No contestar en cualquier otro caso
else:
    print("NO CONTESTAR")