#Contestador de celular
# Pedir al usuario que ingrese el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese el número telefónico: "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar las reglas para decidir si contestar o no
if 0 <= hora_llamada < 7:
    respuesta = "CONTESTAR"  # Llamada entre 00:00 y 07:00
elif hora_llamada < 14 and numero_telefonico % 100 == 909:
    respuesta = "CONTESTAR"  # Llamada antes de las 14:00 y número termina en 909
elif 17 <= hora_llamada < 19 and str(numero_telefonico).startswith("877"):
    respuesta = "NO CONTESTAR"  # Llamada entre 17:00 y 19:00 y número comienza por 877
else:
    respuesta = "NO CONTESTAR"  # Resto de los casos

# Imprimir el resultado
print("Resultado:", respuesta)
