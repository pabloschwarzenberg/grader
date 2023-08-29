#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    binario = bin(numero)[2:]  # Convertir a binario y quitar el prefijo '0b'
    return binario

# Pedir al usuario que ingrese el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", resultado)
