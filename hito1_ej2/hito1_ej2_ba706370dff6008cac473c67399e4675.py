#Contestador de celular
numero_telefonico = input("Ingrese el número telefónico: ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

if hora_llamada >= 0 and hora_llamada < 7:
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico[-3:] != '909':
    print("NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada < 19 and not numero_telefonico.startswith('877'):
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")

