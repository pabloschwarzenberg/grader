def decimal_a_binario(numero_decimal):
    resultado = bin(numero_decimal)[2:]
    return resultado

# Solicitar al usuario que ingrese el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", resultado)
