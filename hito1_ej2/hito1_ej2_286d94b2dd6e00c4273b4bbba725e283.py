#Contestador de celular
numero_telefono = input("Ingrese el número de teléfono (8 dígitos): ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las reglas para decidir si contestar o no
contestar = False

if hora_llamada >= 0 and hora_llamada <= 7:
    contestar = True
elif hora_llamada < 14 and numero_telefono.endswith("909"):
    contestar = True
elif (hora_llamada >= 17 and hora_llamada <= 19) and not numero_telefono.startswith("877"):
    contestar = True

# Imprimir la decisión
if contestar:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
