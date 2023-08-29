# Obtener el número de teléfono y la hora de la llamada
telefono = input("Ingrese el número telefónico: ")
hora = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar si la llamada debe ser contestada
contestar = False

if hora >= 0 and hora < 7:
    contestar = True
elif hora < 14 and telefono[-3:] == '909':
    contestar = True
elif hora >= 17 and hora < 19 and not telefono.startswith('877'):
    contestar = True

# Imprimir el resultado
if contestar:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")


      