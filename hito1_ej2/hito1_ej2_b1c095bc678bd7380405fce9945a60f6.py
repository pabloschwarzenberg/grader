#Contestador de celular
def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"  # Si la llamada ocurre entre 00:00 y 07:00, contestar siempre
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"  # Si la llamada ocurre antes de las 14:00 y el número termina en 909, contestar
    elif hora >= 17 and hora <= 19 and numero // 1000000 == 877:
        return "CONTESTAR"  # Si la llamada ocurre entre 17:00 y 19:00 y el número comienza por 877, contestar
    else:
        return "NO CONTESTAR"  # En cualquier otro caso, no contestar

# Pedir al usuario que ingrese la hora y el número de teléfono
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))
numero_telefono = int(input("Ingrese el número de teléfono (8 dígitos): "))

# Verificar si contestar o no la llamada
respuesta = contestar_llamada(hora_llamada, numero_telefono)

# Mostrar la respuesta
print(respuesta)
      