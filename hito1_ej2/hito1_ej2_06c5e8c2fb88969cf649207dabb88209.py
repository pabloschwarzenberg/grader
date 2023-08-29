#Contestador de celular
# Solicitar al usuario el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (formato 24 horas): "))

# Comprobar las reglas para contestar el celular
if hora_llamada >= 0 and hora_llamada <= 7:
    # Llamada entre 00:00 y 07:00
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    # Llamada antes de las 14:00 y número termina en 909
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico // 1000000 == 877:
    # Llamada entre 17:00 y 19:00 y número comienza por 877
    print("Resultado: CONTESTAR")
else:
    # Resto de los casos
    print("Resultado: NO CONTESTAR")      