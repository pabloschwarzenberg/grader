#Contestador de celular
def contestar_celular(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and str(numero).startswith("877"):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar el número telefónico y la hora al usuario
numero = int(input("Ingrese el número telefónico (8 dígitos): "))
hora = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificar si contestar o no el celular
resultado = contestar_celular(numero, hora)

# Imprimir el resultado
print("Resultado:", resultado)
      