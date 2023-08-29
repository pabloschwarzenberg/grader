#Contestador de celular
def contestar_llamada(hora, numero):
    resto = numero % 1000
    entero = numero // 100000

    if hora >= 0 and hora <= 7:
        return "CONTESTAR"

    elif hora < 14 and resto == 909:
        return "CONTESTAR"

    elif hora >= 17 and hora <= 19 and entero == 877:
        return "NO CONTESTAR"

    else:
        return "NO CONTESTAR"

numero = int(input("Ingrese el número de celular (8 dígitos): "))
hora = int(input("Ingrese la hora (0-23): "))



decision = contestar_llamada(hora, numero)
print(decision)