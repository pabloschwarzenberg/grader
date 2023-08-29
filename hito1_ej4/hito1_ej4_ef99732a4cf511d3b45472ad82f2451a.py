def decimal_a_binario(numero):
    binario = ""
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero_decimal)
print("resultado =", binario)
      