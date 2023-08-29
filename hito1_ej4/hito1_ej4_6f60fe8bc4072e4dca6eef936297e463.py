#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    if decimal == 0:
        return '0'

    resultado = ''
    while decimal > 0:
        resultado = str(decimal % 2) + resultado
        decimal = decimal // 2

    return resultado

numero_decimal = int(input("Ingresa un número decimal: "))
resultado_binario = decimal_a_binario(numero_decimal)

print("Resultado =", resultado_binario)