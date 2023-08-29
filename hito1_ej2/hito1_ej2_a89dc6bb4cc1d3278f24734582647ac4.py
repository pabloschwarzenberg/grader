#Contestador de celular
# Solicitar al usuario que ingrese el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (formato 24 horas): "))

# Verificar las reglas para determinar si se debe contestar la llamada
if hora_llamada >= 0 and hora_llamada < 7:
    # Llamada entre 00:00 y 07:00, contestar siempre
    print("Resultado: CONTESTAR")
elif hora_llamada < 14:
    # Llamada antes de las 14:00, excepto si el número termina en 909
    if numero_telefonico % 1000 == 909:
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada < 19:
    # Llamada entre 17:00 y 19:00, excepto si el número comienza por 877
    if str(numero_telefonico)[0:3] == '877':
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
else:
    # Llamada después de las 19:00, no contestar
    print("Resultado: NO CONTESTAR")
      