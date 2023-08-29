def decimal_a_binario(numero):
    return bin(numero)[2:]

# Solicitar al usuario que ingrese el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", resultado)

      