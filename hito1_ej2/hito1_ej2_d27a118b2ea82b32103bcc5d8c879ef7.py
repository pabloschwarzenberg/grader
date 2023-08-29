def contestar_llamada(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 9:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and numero // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar número telefónico y hora al usuario
numero_telefonico = int(input("Ingrese el número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Determinar si se debe contestar o no
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)