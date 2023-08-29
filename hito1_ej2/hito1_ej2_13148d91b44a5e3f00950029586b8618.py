def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR" # Llamada entre 00:00 y 07:00
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR" # Llamada antes de las 14:00 y número termina en 909
    elif hora >= 17 and hora <= 19 and str(numero).startswith("877"):
        return "NO CONTESTAR" # Llamada durante la tarde y número comienza por 877
    elif hora >= 19:
        return "NO CONTESTAR" # Llamada después de las 19:00
    else:
        return "NO CONTESTAR" # Resto de los casos

# Solicitar la hora y el número de teléfono al usuario
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))
numero_telefono = int(input("Ingrese el número de teléfono (8 cifras): "))

# Determinar si se debe contestar o no la llamada
decision = contestar_llamada(hora_llamada, numero_telefono)

# Mostrar la decisión
print(decision)

Ingrese la hora de la llamada (0-23): 14
Ingrese el número de teléfono (8 cifras): 78735653
NO CONTESTAR
