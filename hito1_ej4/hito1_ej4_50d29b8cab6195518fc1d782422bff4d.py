#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    resultado = bin(numero)[2:]
    return resultado

# Solicitar al usuario el número decimal
numero_decimal = int(input("Ingresa un número decimal: "))

# Convertir a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", resultado_binario)
      