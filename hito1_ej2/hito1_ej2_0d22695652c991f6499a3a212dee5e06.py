#Contestador de celular
# Solicitar número telefónico y hora de la llamada al usuario
numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar las reglas para contestar la llamada
if hora_llamada >= 0 and hora_llamada <= 7:
    # Llamada entre 00:00 y 07:00
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico.endswith("909"):
    # Llamada antes de las 14:00 y número termina en 909
    print("CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19 and not numero_telefonico.startswith("877"):
    # Llamada entre 17:00 y 19:00 y número no comienza por 877
    print("NO CONTESTAR")
else:
    # Resto de los casos
    print("NO CONTESTAR")      