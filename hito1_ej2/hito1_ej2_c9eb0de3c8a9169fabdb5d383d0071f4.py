#Contestador de celular

def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 1000 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and str(numero).startswith("877"):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))
numero_telefono = int(input("Ingrese el número de teléfono que llama (8 dígitos): "))

respuesta = contestar_llamada(hora_llamada, numero_telefono)

print(respuesta)