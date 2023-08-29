def contestar_celular(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14:
        if numero % 1000 == 909:
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    elif hora >= 17 and hora <= 19:
        if str(numero).startswith('877'):
            return "NO CONTESTAR"
        else:
            return "CONTESTAR"
    else:
        return "NO CONTESTAR"


numero_llamada = int(input("Ingresa el número de teléfono (8 dígitos): "))
hora_llamada = int(input("Ingresa la hora de la llamada (0-23): "))

respuesta = contestar_celular(hora_llamada, numero_llamada)
print(respuesta)
