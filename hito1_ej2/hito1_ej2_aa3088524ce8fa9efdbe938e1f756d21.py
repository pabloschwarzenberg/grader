#Contestador de celular
numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar las reglas para determinar si contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 100 == 909:
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico / 10000 % 1 == 877:
    print("Resultado: NO CONTESTAR")
elif hora_llamada >= 14 and hora_llamada < 17 or hora_llamada >= 19:
    print("Resultado: NO CONTESTAR")
else:
    print("Resultado: CONTESTAR")