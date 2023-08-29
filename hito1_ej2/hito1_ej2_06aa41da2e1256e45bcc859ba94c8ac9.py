def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 9:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and str(numero).startswith("877"):
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario que ingrese el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(hora_llamada, numero_telefonico)

# Imprimir el resultado
print("Resultado:", resultado)

# Imprimir el resultado
print("Resultado:", resultado)