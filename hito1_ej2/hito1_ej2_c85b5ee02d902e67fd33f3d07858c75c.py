def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:  # Entre las 00:00 y las 07:00
        return True
    elif hora < 14 :  # Antes de las 14:00
        if numero % 100 == 909:  # El número termina en 909
            return True
        else:
            return False
    elif hora >= 17 and hora < 19:  # Entre las 17:00 y las 19:00
        if numero // 10000000 == 877:  # El número comienza por 877
            return True
        else:
            return False
    else:  # Después de las 19:00
        return False


if contestar_llamada(numero_telefono, hora_llamada):
    print("Contestar llamada")
else:
    print("No contestar llamada")
