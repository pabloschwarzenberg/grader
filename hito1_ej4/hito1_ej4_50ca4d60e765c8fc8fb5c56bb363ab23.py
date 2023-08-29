def decimal_a_binario(numero):
    binario = bin(numero)[2:]
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))

resultado = decimal_a_binario(numero_decimal)

print("Resultado =", resultado)