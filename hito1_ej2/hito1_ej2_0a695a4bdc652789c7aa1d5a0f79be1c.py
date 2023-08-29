#Contestador de celular
 # Solicitar al usuario el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar las reglas para decidir si contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    # Regla 1: Llamada entre 00:00 y 07:00
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    # Regla 2: Llamada antes de las 14:00 y número termina en 909
    print("CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico // 1000000 == 877:
    # Regla 3: Llamada entre 17:00 y 19:00 y número comienza por 877
    print("CONTESTAR")
else:
    # No se cumple ninguna de las reglas anteriores
    print("NO CONTESTAR")
