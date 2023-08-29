#Contestador de celular
def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and str(numero).startswith('877'):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar hora y número telefónico al usuario
hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número de teléfono (8 dígitos): "))

# Determinar si contestar o no
respuesta = contestar_llamada(hora, numero)

# Imprimir resultado
print(respuesta)
      