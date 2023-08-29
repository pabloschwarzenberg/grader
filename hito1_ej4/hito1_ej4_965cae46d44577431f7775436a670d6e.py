#Conversión de Decimal a Binario
def decimal_a_binario(numero):
    if numero == 0:
        return '0'

    resultado = ''
    while numero > 0:
        resultado = str(numero % 2) + resultado
        numero = numero // 2

    return resultado


# Obtener el número decimal de entrada
numero_decimal = int(input("Ingresa un número decimal: "))

# Convertir el número decimal a binario
resultado_binario = decimal_a_binario(numero_decimal)

# Imprimir el resultado
print("resultado =", resultado_binario)
