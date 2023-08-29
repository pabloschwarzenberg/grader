#Contestador de celular
      # Solicitar al usuario que ingrese el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

# Verificar las reglas para decidir si contestar o no
if hora_llamada >= 0 and hora_llamada < 7:
    # Llamada entre las 00:00 y las 07:00
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 100 == 9:
    # Llamada antes de las 14:00 y número termina en 909
    print("CONTESTAR")
elif hora_llamada >= 17 and hora_llamada < 19 and numero_telefonico // 1000000 == 877:
    # Llamada entre las 17:00 y las 19:00 y número comienza por 877
    print("CONTESTAR")
else:
    # No contestar en los demás casos
    print("NO CONTESTAR")
