#Contestador de celular
def contestar_celular(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 9:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and numero // 1000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero = int(input("Ingrese el número de celular (8 dígitos): "))
hora = int(input("Ingrese la hora (0-23): "))

decision = contestar_celular(hora, numero)
print(decision)