def contestar_celular(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"  # Si la llamada ocurre entre 00:00 y 07:00, contestar siempre
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"  # Si ocurre antes de las 14:00 y el número termina en 909, contestar
    elif hora >= 17 and hora <= 19 and numero // 10000000 == 877:
        return "CONTESTAR"  # Durante la tarde (17:00 - 19:00), contestar si el número comienza por 877
    else:
        return "NO CONTESTAR"  # En todos los demás casos, no contestar

# Solicitar la hora del día y el número de celular al usuario
hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número de celular (8 cifras): "))

# Determinar si contestar o no
respuesta = contestar_celular(hora, numero)

# Imprimir el resultado
print(respuesta)



