#Contestador de celular
def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"  # Se contesta si la llamada ocurre entre 00:00 y 07:00
    elif hora < 14 and numero[-3:] == '909':
        return "CONTESTAR"  # Se contesta si la llamada ocurre antes de las 14:00 y el número termina en 909
    elif hora >= 17 and hora <= 19 and numero[:3] == '877':
        return "CONTESTAR"  # Se contesta si la llamada ocurre entre 17:00 y 19:00 y el número comienza por 877
    else:
        return "NO CONTESTAR"  # No se contesta en los demás casos

# Pedimos al usuario que ingrese la hora y el número de teléfono
hora = int(input("Ingrese la hora (0-23): "))
numero = input("Ingrese el número de teléfono (8 dígitos): ")

# Verificamos si se debe contestar o no la llamada
respuesta = contestar_llamada(hora, numero)

# Imprimimos la respuesta
print(respuesta)