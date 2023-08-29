#Contestador de celular
numero_telefonico = input("Ingrese el número telefónico: ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

if hora_llamada >= 0 and hora_llamada <= 7:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and not numero_telefonico.endswith('909'):
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico.startswith('877'):
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
