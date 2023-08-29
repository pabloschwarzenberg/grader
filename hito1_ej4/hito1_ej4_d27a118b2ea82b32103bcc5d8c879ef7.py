def decimal_a_binario(numero_decimal):
    binario = bin(numero_decimal)[2:]  # Utilizamos la función 'bin' para convertir a binario y eliminamos el prefijo '0b'
    return binario

# Solicitar número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", resultado)    