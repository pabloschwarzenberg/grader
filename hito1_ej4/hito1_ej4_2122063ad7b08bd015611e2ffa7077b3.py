#Conversión de Decimal a Binario
def decimal_a_binario(decimal):
    binario = ""
    if decimal == 0:
        binario = "0"
    else:
        while decimal > 0:
            residuo = decimal % 2
            binario = str(residuo) + binario
            decimal = decimal // 2
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))

resultado_binario = decimal_a_binario(numero_decimal)

print("Resultado =", resultado_binario)