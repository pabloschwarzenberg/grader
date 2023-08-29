def contestar_llamada(numero_telefonico, hora_llamada):
    numero_telefonico = int(numero_telefonico)
    hora_llamada = int(hora_llamada)

    if hora_llamada >= 0 and hora_llamada <= 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and numero_telefonico % 1000 == 909:
        return "CONTESTAR"
    elif (hora_llamada >= 17 and hora_llamada <= 19) and not str(numero_telefonico).startswith("877"):
        return "NO CONTESTAR"
    else:
        return "CONTESTAR"

# Solicitar al usuario el número telefónico y la hora de la llamada
numero_telefonico = input("Ingrese el número telefónico (8 cifras): ")
hora_llamada = input("Ingrese la hora de la llamada (0-23): ")

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)
