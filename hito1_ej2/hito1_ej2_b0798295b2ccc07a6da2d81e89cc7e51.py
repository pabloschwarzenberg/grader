def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and str(numero).startswith("877"):
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Ejemplo de uso
hora = int(input("Ingrese la hora del día (entre 0 y 23): "))
numero = int(input("Ingrese el número de celular que llama (8 dígitos): "))

resultado = contestar_llamada(hora, numero)
print(resultado)
