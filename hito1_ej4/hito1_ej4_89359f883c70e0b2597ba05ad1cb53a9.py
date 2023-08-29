def decimal_a_binario(numero):
    binario = bin(numero)[2:]  # Utilizamos la función bin() para obtener la representación binaria y eliminamos los dos primeros caracteres "0b"
    return binario


# Solicitar el número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Mostrar el resultado en pantalla
print("Resultado =", resultado_binario)
    