#Conversión de Decimal a Binario
def decimal_a_binario(numero_decimal):
    resultado = bin(numero_decimal)[2:]
    return resultado

# Solicitar al usuario que ingrese un número decimal
numero_decimal = int(input("Ingrese un número decimal: "))

# Convertir el número decimal a binario llamando a la función
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado de la conversión
print("resultado =", resultado_binario)      