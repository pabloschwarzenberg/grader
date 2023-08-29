def decimal_a_binario(decimal):
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))
numero_binario = decimal_a_binario(numero_decimal)
print("resultado=" + numero_binario)