def contestar_llamada(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14:
        if numero[-3:] == "909":
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    elif hora >= 17 and hora <= 19:
        if numero[:3] == "877":
            return "NO CONTESTAR"
        else:
            return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar el número telefónico al usuario
numero_telefonico = input("Ingrese número telefónico (8 dígitos): ")

# Solicitar la hora de la llamada al usuario
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)
