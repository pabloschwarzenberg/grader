def decimal_a_binario(numero):
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))
resultado = decimal_a_binario(numero_decimal)
print("resultado =", resultado)