def contestar_llamada(numero_telefonico, hora_llamada):
    numero_telefonico = int(numero_telefonico)
    hora_llamada = int(hora_llamada)

    if hora_llamada >= 0 and hora_llamada <= 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and str(numero_telefonico)[-3:] == "909":
        return "CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada <= 19 and str(numero_telefonico).startswith("877"):
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = input("Ingrese el número telefónico (8 dígitos): ")
hora_llamada = input("Ingrese la hora de la llamada (0-23): ")

resultado = contestar_llamada(numero_telefonico, hora_llamada)

print("Resultado:", resultado)
