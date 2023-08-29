#Contestador de celular
def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and not str(numero)[-3:] == "909":
        return "NO CONTESTAR"
    elif hora >= 17 and hora < 19 and not str(numero).startswith("877"):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario la hora y el número de teléfono
hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número de teléfono (8 dígitos): "))

# Verificar si se debe contestar la llamada
respuesta = contestar_llamada(hora, numero)

# Imprimir la respuesta
print(respuesta)
      