def decimal_a_binario(numero):
    binario = bin(numero)[2:]  # Utilizamos la función bin() para obtener la representación binaria y eliminamos el prefijo "0b"
    return binario

# Solicitar al usuario el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", resultado)
