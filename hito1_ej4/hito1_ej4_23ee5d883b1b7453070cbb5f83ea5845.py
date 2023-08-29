#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))
resultado = decimal_a_binario(numero_decimal)
print("resultado =", resultado)