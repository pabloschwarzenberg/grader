def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and str(numero).startswith("877"):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"


# Pedir al usuario el número telefónico y la hora de la llamada
numero = int(input("Ingrese número telefónico (8 cifras): "))
hora = int(input("Ingrese la hora de la llamada (0-23): "))

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(numero, hora)

# Imprimir el resultado
print("Resultado:", resultado)