#Contestador de celular
     # Solicitar al usuario ingresar el número telefónico y la hora de la llamada
numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada: "))

# Verificar si se debe contestar la llamada
contestar = False

if hora_llamada >= 0 and hora_llamada < 7:
    contestar = True
elif hora_llamada < 14 and numero_telefonico[-3:] == '909':
    contestar = True
elif hora_llamada >= 17 and hora_llamada < 19 and numero_telefonico.startswith('877'):
    contestar = False  # Excepción: No contestar si el número comienza con 877
else:
    contestar = False

# Imprimir el resultado
if contestar:
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
