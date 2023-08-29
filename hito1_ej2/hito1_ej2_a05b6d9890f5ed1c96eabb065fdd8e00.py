#Contestador de celular
def contestar_celular(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14:
        if str(numero)[-3:] == "909":
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    elif hora >= 17 and hora <= 19:
        if str(numero).startswith("877"):
            return "NO CONTESTAR"
        else:
            return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario el número telefónico y la hora de la llamada
numero = input("Ingrese número telefónico (8 cifras): ")
hora = int(input("Ingrese la hora de la llamada (0-23): "))

# Obtener la respuesta automática
resultado = contestar_celular(numero, hora)

# Imprimir el resultado
print("Resultado:", resultado)