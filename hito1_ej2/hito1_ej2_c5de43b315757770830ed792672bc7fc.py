def contestar_celular(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 10000 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and str(numero).startswith("877"):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"


# Ejemplo de uso
hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número de celular (8 dígitos): "))

decision = contestar_celular(hora, numero)
print(decision)
