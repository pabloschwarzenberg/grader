def contestar_celular(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14:
        if numero % 1000 == 909:
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    elif hora >= 17 and hora <= 19:
        if numero // 10000000 == 877:
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefono = int(input("Ingrese el número de celular (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

respuesta = contestar_celular(numero_telefono, hora_llamada)
print(respuesta)
