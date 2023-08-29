def decimalabinaio(decimal):
    resultado = ""
    while decimal > 0:
        residuo = decimal % 2
        resultado = resultado + str(residuo)
        decimal = decimal // 2
    return resultado[::-1]

numero = int(input("Ingresa el decimal para convertir: "))

print("Resultado =",decimalabinaio(numero))