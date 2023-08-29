def contestar_llamada(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada < 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and str(numero_telefonico)[-3:] == "909":
        return "CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada < 19 and str(numero_telefonico)[:3] == "877":
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario el número de teléfono y la hora de la llamada
numero_telefonico = int(input("Ingrese el número telefónico: "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar si se debe contestar o no la llamada
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)
