def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]  
    return binario

numero_decimal = int(input("Ingresa un número decimal: "))

resultado = decimal_a_binario(numero_decimal)

print("Resultado =", resultado)