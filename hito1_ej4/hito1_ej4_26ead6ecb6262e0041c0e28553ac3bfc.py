def decimal_a_binario(numero_decimal):
    resultado = bin(numero_decimal)[2:]  # Convertir a binario y eliminar el prefijo "0b"
    return resultado


# Solicitar al usuario que ingrese un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado en pantalla
print("Resultado =", resultado_binario)
