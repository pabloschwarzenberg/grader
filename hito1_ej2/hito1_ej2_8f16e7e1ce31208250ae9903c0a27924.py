# Obtener los datos del usuario
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar si contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    resultado = "CONTESTAR"
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    resultado = "CONTESTAR"
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico // 10000000 == 877:
    resultado = "CONTESTAR"
else:
    resultado = "NO CONTESTAR"

# Imprimir el resultado
print("Resultado:", resultado)
