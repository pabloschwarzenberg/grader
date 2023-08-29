#Contestador de celular

# Solicitar el número de teléfono y la hora de la llamada al usuario
numero_telefono = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar las reglas para contestar la llamada
contestar = False

if hora_llamada >= 0 and hora_llamada <= 7:
    contestar = True
elif hora_llamada < 14 and numero_telefono % 100 == 909:
    contestar = True
elif hora_llamada >= 17 and hora_llamada <= 19 and str(numero_telefono)[0:3] == "877":
    contestar = True

# Mostrar el resultado
if contestar:
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")