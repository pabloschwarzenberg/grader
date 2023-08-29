def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"  # Llamada entre 00:00 y 07:00
    elif hora < 14 and numero % 1000 == 909:
        return "CONTESTAR"  # Llamada antes de las 14:00 y número termina en 909
    elif hora >= 17 and hora <= 19 and numero // 1000000 == 877:
        return "CONTESTAR"  # Llamada entre 17:00 y 19:00 y número comienza por 877
    else:
        return "NO CONTESTAR"  # Resto de los casos


hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número de teléfono (8 dígitos): "))

resultado = contestar_llamada(hora, numero)
print(resultado)

      