def decimal_a_binario(numero):
    resultado = bin(numero)[2:]  # Utilizamos la función bin() para convertir a binario y omitimos los primeros dos caracteres '0b'
    return resultado

# Solicitar el número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Llamar a la función y mostrar el resultado
resultado_binario = decimal_a_binario(numero_decimal)
print("Resultado =", resultado_binario)
