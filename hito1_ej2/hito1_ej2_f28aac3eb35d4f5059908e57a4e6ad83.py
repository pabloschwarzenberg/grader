def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 1000 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and str(numero).startswith("877"):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar al usuario el número de teléfono y la hora de la llamada
numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada: "))

# Verificar si contestar o no
resultado = contestar_llamada(hora, numero)

# Imprimir el resultado
print("Resultado:", resultado)      