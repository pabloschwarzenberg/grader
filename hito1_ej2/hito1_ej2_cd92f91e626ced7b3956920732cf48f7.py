#contestador automatico
def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and str(numero).startswith('877'):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"


# Solicitar al usuario ingresar el número de teléfono y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

# Determinar si se debe contestar o no la llamada
resultado = contestar_llamada(hora_llamada, numero_telefonico)

# Imprimir el resultado
print("Resultado:", resultado)
