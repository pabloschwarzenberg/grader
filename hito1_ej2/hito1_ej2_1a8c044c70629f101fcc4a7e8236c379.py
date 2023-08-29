#Inicio
#Solicitar el número de teléfono y la hora de la llamada al usuario
numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

#Verificar las reglas para contestar la llamada
if hora_llamada >= 0 and hora_llamada < 7:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada < 19 and numero_telefonico // 10000000 == 877:
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")
    
#Fin