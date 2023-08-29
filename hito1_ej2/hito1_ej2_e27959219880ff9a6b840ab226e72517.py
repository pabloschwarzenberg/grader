def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"  # Llamada entre 00:00 y 07:00
    elif hora < 14 and numero==909:
        return "CONTESTAR"  # Llamada antes de las 14:00 y número termina en 909
    elif hora >= 17 and hora <= 19 and str(numero).startswith("877"):
        return "CONTESTAR"  # Llamada entre 17:00 y 19:00 y número comienza con 877
    else:
        return "NO CONTESTAR"  # Resto de los casos

# Solicitar al usuario la hora del día y el número de celular
hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número de celular (8 dígitos): "))

# Determinar si se debe contestar la llamada
respuesta = contestar_llamada(hora, numero)

# Imprimir la respuesta
print(respuesta)
