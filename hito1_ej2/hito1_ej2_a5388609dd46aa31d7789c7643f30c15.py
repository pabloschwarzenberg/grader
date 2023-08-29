def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14:
        if numero % 1000 == 909:
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    elif hora >= 17 and hora < 19:
        if str(numero).startswith('877'):
            return "NO CONTESTAR"
        else:
            return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario ingresar el número de teléfono y la hora de la llamada
numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar si se debe contestar o no la llamada
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)