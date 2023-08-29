def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]
    return binario

# Solicitar número decimal al usuario
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", resultado)
      