def contestar_celular(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada < 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and numero_telefonico % 1000 == 909:
        return "CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada < 19 and numero_telefonico // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))
resultado = contestar_celular(numero_telefonico, hora_llamada)
print("Resultado:", resultado)