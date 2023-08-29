# Ingresar el número telefónico
numero_telefonico = int(input("Ingrese número telefónico: "))

# Ingresar la hora de la llamada
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar las reglas para contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico // 1000000 == 877:
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")