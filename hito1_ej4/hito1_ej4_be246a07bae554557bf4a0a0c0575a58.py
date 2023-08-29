def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]
    return binario

# Solicitar el número decimal al usuario
numero_decimal = int(input("Ingresa un número decimal: "))

# Convertir el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", resultado_binario)
      