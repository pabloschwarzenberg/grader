#Contestador de celular
# Obtener el número telefónico y la hora de la llamada del usuario
numero_telefonico = input("Ingrese el número telefónico (8 dígitos): ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar si se debe contestar o no la llamada
contestar = False

if hora_llamada >= 0 and hora_llamada <= 7:
    contestar = True
elif hora_llamada < 14 and numero_telefonico[-3:] == '909':
    contestar = True
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico.startswith('877'):
    contestar = False

# Imprimir el resultado
if contestar:
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
