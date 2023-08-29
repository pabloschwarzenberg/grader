def decimal_a_binario(numero):
    return bin(numero)[2:]  # Eliminamos los dos primeros caracteres '0b' del resultado binario


# Pedir al usuario el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
numero_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", numero_binario)