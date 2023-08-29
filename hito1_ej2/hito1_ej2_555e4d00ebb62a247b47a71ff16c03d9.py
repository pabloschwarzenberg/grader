# Solicitar al usuario el número telefonico y la hora de la llamada
numero_telefonico = int(input("Ingrese el número telefonico (8 digitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las reglas para determinar si se contesta o no
if hora_llamada >= 0 and hora_llamada <= 7:
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    print("CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico // 10000000 == 877:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
      