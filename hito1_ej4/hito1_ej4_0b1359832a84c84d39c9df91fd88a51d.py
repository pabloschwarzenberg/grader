#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    binario = bin(numero)[2:]
    return binario

# Solicitar al usuario ingresar un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
numero_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("Resultado =", numero_binario)     