#Contestador de celular
def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and numero // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario el número telefónico y la hora de la llamada
numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada (0-23): "))

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(hora, numero)

# Imprimir el resultado
print("Resultado:", resultado)
