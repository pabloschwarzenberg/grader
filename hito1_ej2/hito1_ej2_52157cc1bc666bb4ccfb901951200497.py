#Contestador de celular
def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and str(numero)[-3:] == "909":
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and str(numero)[:3] != "877":
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario el número telefónico y la hora de la llamada
numero = int(input("Ingrese el número telefónico (8 dígitos): "))
hora = int(input("Ingrese la hora de la llamada (entre 0 y 23): "))

# Determinar si se debe contestar o no la llamada
respuesta = contestar_llamada(hora, numero)

# Imprimir la respuesta
print("Resultado:", respuesta)