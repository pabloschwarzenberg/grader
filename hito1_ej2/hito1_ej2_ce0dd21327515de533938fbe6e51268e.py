#Contestador de celular
def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"  # Llamada entre 00:00 y 07:00, siempre contestar
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"  # Llamada antes de las 14:00 y número termina en 909, contestar
    elif hora >= 17 and hora < 19 and str(numero).startswith("877"):
        return "CONTESTAR"  # Llamada entre 17:00 y 19:00 y número comienza por 877, contestar
    else:
        return "NO CONTESTAR"  # No se cumplen las condiciones, no contestar

# Solicitar al usuario la hora y el número de teléfono
hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número de teléfono (8 dígitos): "))

# Determinar si se debe contestar o no
respuesta = contestar_llamada(hora, numero)

# Imprimir el resultado
print(respuesta)
