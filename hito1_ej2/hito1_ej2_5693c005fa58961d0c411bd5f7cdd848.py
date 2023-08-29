#Contestador de celular
def contestar_llamada(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 1000 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and numero // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Pedimos al usuario que ingrese el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificamos si se debe contestar o no la llamada
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimimos el resultado
print("Resultado:", resultado)      