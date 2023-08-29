def decimal_a_binario(numero_decimal):
    resultado_binario = ""
    while numero_decimal > 0:
        resultado_binario = str(numero_decimal % 2) + resultado_binario
        numero_decimal = numero_decimal // 2
    return resultado_binario

numero_decimal = int(input("Ingrese un número decimal: "))
resultado = decimal_a_binario(numero_decimal)
print("resultado=" + resultado)
