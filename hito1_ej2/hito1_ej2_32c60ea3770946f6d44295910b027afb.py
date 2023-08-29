#Contestador de celular
def contestar_telefono(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and str(numero)[-3:] == "909":
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and str(numero).startswith("877"):
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario ingresar el número de teléfono y la hora de la llamada
numero_telefono = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar si se debe contestar o no
resultado = contestar_telefono(numero_telefono, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)
