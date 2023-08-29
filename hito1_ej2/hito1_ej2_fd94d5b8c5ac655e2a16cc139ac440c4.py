def contestar_llamada(hora, numero):
    """
    Función para determinar si se debe contestar una llamada telefónica
    basándose en la hora y el número de teléfono.

    Argumentos:
    - hora: entero representando la hora del día (entre 0 y 23)
    - numero: entero representando el número de teléfono (de 8 cifras)

    Retorna:
    - respuesta: string indicando si se debe "CONTESTAR" o "NO CONTESTAR" la llamada
    """
    if hora >= 0 and hora <= 7:
        # Llamada entre 00:00 y 07:00
        respuesta = "CONTESTAR"
    elif hora < 14:
        # Llamada antes de las 14:00
        if numero % 1000 == 909:
            # El número termina en 909
            respuesta = "CONTESTAR"
        else:
            respuesta = "NO CONTESTAR"
    elif hora >= 17 and hora <= 19:
        # Llamada entre 17:00 y 19:00
        if str(numero).startswith('877'):
            # El número comienza por 877
            respuesta = "NO CONTESTAR"
        else:
            respuesta = "CONTESTAR"
    else:
        # Llamada después de las 19:00
        respuesta = "NO CONTESTAR"

    return respuesta

# Solicitar el número de teléfono y la hora de la llamada al usuario
numero = int(input("Ingrese el número telefónico (8 cifras): "))
hora = int(input("Ingrese la hora de la llamada (entre 0 y 23): "))

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(hora, numero)

# Mostrar el resultado
print("Resultado:", resultado)


      