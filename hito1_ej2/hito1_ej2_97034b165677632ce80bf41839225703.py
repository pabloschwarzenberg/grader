def contestar_celular(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and str(numero).endswith("909"):
          return "CONTESTAR"
    elif hora >= 17 and hora <= 19:
        if str(numero).startswith("877"):
            return "NO CONTESTAR"
        else:
            return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario que ingrese la hora y el número de celular
numero_celular = int(input("Ingrese el número de celular que llama: "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Determinar si se debe contestar o no
respuesta = contestar_celular(numero_celular, hora_llamada)

# Imprimir la respuesta
print(respuesta)
