def decimal_a_binario(decimal):

    if decimal == 0:
        return '0'

    binario = []

    while decimal > 0:
        residuo = decimal % 2
        binario.append(str(residuo))
        decimal = decimal // 2

    binario.reverse()

    return ''.join(binario)

decimal = int(input("Ingrese un número decimal: "))

resultado = decimal_a_binario(decimal)

print("Resultado =", resultado)      