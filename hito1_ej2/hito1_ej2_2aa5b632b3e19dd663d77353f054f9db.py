def contestar_llamada(numero, hora):
    numero = int(numero)
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 1000 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and str(numero).startswith("877"):
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario ingresar el número de teléfono y la hora de la llamada
numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(numero_telefonico, hora_llamada)
print("Resultado:", resultado)
