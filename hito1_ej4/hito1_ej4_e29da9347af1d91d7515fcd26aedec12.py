def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"
    binario = ""
    while decimal > 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))
resultado_binario = decimal_a_binario(numero_decimal)
print("resultado=" + resultado_binario)
