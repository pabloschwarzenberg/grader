def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and numero // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar el número telefónico y la hora al usuario
numero = input("Ingrese el número telefónico (8 dígitos): ")
hora = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar si se debe contestar o no la llamada
resultado = contestar_llamada(int(numero), hora)

# Imprimir el resultado
print("Resultado:", resultado)