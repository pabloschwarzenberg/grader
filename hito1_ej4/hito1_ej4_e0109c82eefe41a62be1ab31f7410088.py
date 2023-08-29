#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    return bin(numero)[2:]

# Solicitar al usuario ingresar el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", resultado)

      