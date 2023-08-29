#Contestador de celular
def contestar_llamada(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada < 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and str(numero_telefonico)[-3:] == "909":
        return "CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada < 19 and not str(numero_telefonico).startswith("877"):
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

# Pedir al usuario que ingrese el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)
