numero_telefonico = input("Ingrese el número telefónico (8 dígitos): ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

def contestar_llamada(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada <= 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and numero_telefonico.endswith("909"):
        return "CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico.startswith("877"):
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"


resultado = contestar_llamada(numero_telefonico, hora_llamada)
print("Resultado:", resultado)
