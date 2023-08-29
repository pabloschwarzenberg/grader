#Contestador de celular

def contestar_celular(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and str(numero)[-3:] == "909":
        return "CONTESTAR"
    elif (hora >= 17 and hora <= 19) or str(numero)[:3] != "877":
        return "NO CONTESTAR"
    else:
        return "CONTESTAR"

# Solicitar número telefónico y hora de la llamada al usuario
numero = int(input("Ingrese número telefónico (8 dígitos): "))
hora = int(input("Ingrese hora de la llamada (0-23): "))

# Obtener resultado
resultado = contestar_celular(hora, numero)

# Imprimir resultado
print("Resultado:", resultado)
