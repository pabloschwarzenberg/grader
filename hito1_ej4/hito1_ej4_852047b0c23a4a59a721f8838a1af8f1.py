def decimal_a_binario(decimal):
    return bin(decimal)[2:]

numero_decimal = int(input("Ingresa un número decimal: "))
numero_binario = decimal_a_binario(numero_decimal)

print("resultado=", numero_binario)