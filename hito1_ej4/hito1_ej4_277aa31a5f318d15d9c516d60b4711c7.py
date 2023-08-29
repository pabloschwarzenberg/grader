def decimal_a_binario(numero_decimal):
    binario = bin(numero_decimal)[2:]
    return binario

numero_decimal = int(input("ingresa un numero decimal: "))

resultado_binario = decimal_a_binario(numero_decimal)

print("Resultado=", resultado_binario)