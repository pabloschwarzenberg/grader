# Solicitar el número telefónico y la hora de la llamada al usuario
numero_telefonico = input("Ingrese el número telefónico (8 dígitos): ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las reglas para contestar o no la llamada
if 0 <= hora_llamada <= 7:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and numero_telefonico[-3:] == '909':
    print("Resultado: CONTESTAR")
elif 17 <= hora_llamada <= 19 and numero_telefonico[:3] != '877':
    print("Resultado: NO CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
