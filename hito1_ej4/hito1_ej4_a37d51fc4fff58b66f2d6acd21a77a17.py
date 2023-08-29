#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = bin(decimal)[2:]
    return binario

# Solicitar al usuario el número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print(resultado_binario)
