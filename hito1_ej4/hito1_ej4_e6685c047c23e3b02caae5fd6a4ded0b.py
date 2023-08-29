def decimal_a_binario(numero):
    numero_decimal = int(numero)
    numero_binario = bin(numero_decimal)[2:]  # El prefijo "0b" se omite
    return numero_binario


numero_decimal = input("Ingrese un número decimal: ")
numero_binario = decimal_a_binario(numero_decimal)
print(numero_binario)
