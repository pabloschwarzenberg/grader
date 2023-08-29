#Conversión de Decimdef decimal_a_binario(decimal):
def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"

    binario = ""

    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2

    return binario


# Ejemplo de uso
decimal = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(decimal)
(print("resultado =", int(binario)))
