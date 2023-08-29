def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    
    binario = ''
    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero //= 2
    
    return binario

numero_decimal = int(input("Ingrese un número decimal: "))

resultado_binario = decimal_a_binario(numero_decimal)

print("Resultado =", resultado_binario)

      