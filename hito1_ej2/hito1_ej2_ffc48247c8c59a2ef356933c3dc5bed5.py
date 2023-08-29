def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:  # Llamada entre 00:00 y 07:00
        return "CONTESTAR"
    elif hora < 14 and numero[-3:] == '909':  # Llamada antes de las 14:00 y número termina en 909
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and numero[:3] == '877':  # Llamada entre 17:00 y 19:00 y número comienza por 877
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar entrada al usuario
hora_llamada = int(input("Ingrese la hora (0-23) de la llamada: "))
numero_telefono = input("Ingrese el número de teléfono (8 dígitos): ")

# Verificar si contestar o no
resultado = contestar_llamada(hora_llamada, numero_telefono)
print(resultado)
