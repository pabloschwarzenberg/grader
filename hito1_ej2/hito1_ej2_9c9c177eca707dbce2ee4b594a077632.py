#Contestador de celular
# Solicitar al usuario el número telefónico y la hora de la llamada
numero_telefonico = input("Ingrese el número telefónico (8 cifras): ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las reglas para determinar si contestar o no
if hora_llamada >= 0 and hora_llamada < 7:
    # Llamada entre 00:00 y 07:00
    print("Resultado: CONTESTAR")
elif hora_llamada > 6 and hora_llamada < 14:
    print("Resultado: CONTESTAR")
     # Llamada antes de las 14:00, excepto si el número termina en 909
elif not numero_telefonico.endswith("909"):
  print("Resultado: NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19:
    print("Resultado: CONTESTAR")
    # Llamada entre 17:00 y 19:00, excepto si el número comienza por 877
elif not numero_telefonico.startswith("877"):
    print("Resultado: NO CONTESTAR")
elif hora_llamada > 19 and hora_llamada < 0:
    # Llamada después de las 19:00
    print("Resultado: NO CONTESTAR")