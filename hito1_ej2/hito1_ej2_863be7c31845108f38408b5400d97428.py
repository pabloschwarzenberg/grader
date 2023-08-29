#Contestador de celular
# Pedir al usuario que ingrese el número telefónico y la hora de la llamada
# Solicitar a usurio ingresar numero telefonico y hora de llamada:
numero_telefonico = input("Ingrese el número telefónico (8 cifras): ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las reglas para determinar si contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico[-3:] == '909':
    print("CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico[:3] != '877':
    print("CONTESTAR")
else:
    print("NO CONTESTAR")      