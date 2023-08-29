#Contestador de celular
numero_telefono = int(input("Ingrese el número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

if hora_llamada >= 0 and hora_llamada <= 7:
    # Llamada entre 00:00 y 07:00
    print("Contestar la llamada (posible emergencia)")

elif hora_llamada < 14:
    # Llamada antes de las 14:00
    if numero_telefono % 100 == 909:
        print("Contestar la llamada (número termina en 909)")
    else:
        print("No contestar la llamada")

elif hora_llamada >= 17 and hora_llamada <= 19:
    # Llamada entre 17:00 y 19:00
    if str(numero_telefono).startswith("877"):
        print("Contestar la llamada (número comienza por 877)")
    else:
        print("No contestes la llamada")

else:
    # Llamada después de las 19:00
    print("No contestes la llamada")
      