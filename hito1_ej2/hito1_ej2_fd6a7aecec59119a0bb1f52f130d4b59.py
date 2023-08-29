def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and str(numero)[-3:] == "909":
        return "CONTESTAR"
    elif hora < 14:
        return "NO CONTESTAR"
    elif hora >= 17 and hora < 19 and not str(numero).startswith("877"):
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar el número telefónico y la hora de la llamada al usuario
numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Determinar si se contesta o no la llamada
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)
  