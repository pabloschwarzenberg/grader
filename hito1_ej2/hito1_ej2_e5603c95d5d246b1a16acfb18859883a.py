#Contestador de celular
# Solicitar al usuario que ingrese el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar las reglas para determinar si se debe contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    # Regla: Llamada entre 00:00 y 07:00
    print("Resultado: CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 1000 == 909:
    # Regla: Llamada antes de las 14:00, número termina en 909
    print("Resultado: CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and not str(numero_telefonico).startswith("877"):
    # Regla: Llamada entre 17:00 y 19:00, número no comienza con 877
    print("Resultado: CONTESTAR")
else:
    # Regla: Llamada después de las 19:00
    print("Resultado: NO CONTESTAR")
      